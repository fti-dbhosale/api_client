import os
import pyinotify
from s3_uploader import upload_to_s3

directory_path = "images"
class EventProcessor(pyinotify.ProcessEvent):
    _methods = ["IN_CREATE",
                "IN_OPEN",
                "IN_ACCESS",
                "IN_ATTRIB",
                "IN_CLOSE_NOWRITE",
                "IN_CLOSE_WRITE",
                "IN_DELETE",
                "IN_DELETE_SELF",
                "IN_IGNORED",
                "IN_MODIFY",
                "IN_MOVE_SELF",
                "IN_MOVED_FROM",
                "IN_MOVED_TO",
                "IN_Q_OVERFLOW",
                "IN_UNMOUNT",
                "default"]

def process_generator(cls, method):
    def _method_name(self, event):
        if method ==  "IN_CREATE" and ( event.pathname[-3:] != "swp" and event.pathname[-3:] != "swx" ):
            print("Method name: process_{}()\n"
                  "Path name: {}\n"
                  "Event Name: {}\n".format(method, event.pathname, event.maskname))
            upload_to_s3(event.pathname, directory_path)
    _method_name.__name__ = "process_{}".format(method)
    setattr(cls, _method_name.__name__, _method_name)

for method in EventProcessor._methods:
    process_generator(EventProcessor, method)

watch_manager = pyinotify.WatchManager()
event_notifier = pyinotify.Notifier(watch_manager, EventProcessor())

watch_this = os.path.abspath(directory_path)
watch_manager.add_watch(watch_this, pyinotify.ALL_EVENTS)
event_notifier.loop()
