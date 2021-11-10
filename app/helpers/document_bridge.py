#!pip install boto3[crt]

import logging
import boto3
from botocore.exceptions import ClientError
import os

class S3DocumentBridge:
  bucket = None
  def __init__(self, bucket):
    self.bucket = bucket
  
  def save(self, file_name):
    object_name = os.path.basename(file_name)
    
    # Upload the file
    s3_client = boto3.client('s3')
    try:
      response = s3_client.upload_file(file_name, self.bucket, object_name)
    except ClientError as e:
      logging.error(e)
      return False
    return True
  
  def get(self, file_name):
    object_name = os.path.basename(file_name)
    s3 = boto3.client('s3')
    s3.download_file(self.bucket, object_name, file_name)
