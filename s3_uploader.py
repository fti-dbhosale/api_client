import boto3

ACCESS_KEY = 'AKIARZC2K5VUDENYQQTH'
SECRET_KEY = '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'
BUCKET_NAME = 'images-api-upload'

def upload_to_s3(filename, filepath):
    s3_client = boto3.client('s3',
                        aws_access_key_id=ACCESS_KEY,
                        aws_secret_access_key=SECRET_KEY
                        )
    try:
        s3_response = s3_client.upload_file(filename ,BUCKET_NAME ,filename.split('/')[-1])
        print("File : {} uploaded at Bucket : {}".format( filename.split('/')[-1], BUCKET_NAME ))
    except Exception as e:
        raise IOError(e)
    response = { 'body': {
            'file_path': filename.split('/')[-1],
            'bucket_name': BUCKET_NAME
                }
            }
    return response
