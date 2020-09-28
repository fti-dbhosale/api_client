import boto3
import json
from api_client import put_data

ACCESS_KEY = 'AKIARZC2K5VUDENYQQTH'
SECRET_KEY = '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'
BUCKET_NAME = 'images-api-upload'

def upload_to_s3(filename, filepath):
    response = {}
    s3_client = boto3.client('s3',
                        aws_access_key_id=ACCESS_KEY,
                        aws_secret_access_key=SECRET_KEY
                        )
    try:
        s3_response = s3_client.upload_file(filename ,BUCKET_NAME ,filename.split('/')[-1])
        filepath = filename
        filename = filename.split('/')[-1]
        filepath = filename.replace(filename.split('/')[-1], "")
        response = put_data(BUCKET_NAME, filepath, filename)
        print("File : {} uploaded at Bucket : {}".format( filename.split('/')[-1], BUCKET_NAME ))
    except Exception as e:
        response = put_data()
        response["File_Path"] = filename
        response["Error"] = e
        raise IOError(e)
    return response
