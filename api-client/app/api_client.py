from datetime import datetime
from pytz import timezone
import requests
import json

API_ENDPOINT = "https://vze0vcujz5.execute-api.ap-south-1.amazonaws.com/dev/markerlog"

def put_data(s3_bucket="", filepath="", filename=""):
    now = datetime.now().astimezone(timezone('Asia/Kolkata'))
    now = now.strftime('%Y-%m-%d %H:%M:%S')
    data = { "DeviceID": "VT_70da6d02-acba-40e2-9c05-402e7f9f290a.DEB-NUC8i3BE-G6BE01300NXK",
             "RecordID": now,
             "S3":{
                    "Bucket": s3_bucket,
                    "Prefix": filepath
                 },
             "payload": {
                    "Action": "Waching",
                    "Snapshot": filename
                 }
            }
    response =  requests.post(API_ENDPOINT , json = data)
    response = json.loads(response.text)
    return response

