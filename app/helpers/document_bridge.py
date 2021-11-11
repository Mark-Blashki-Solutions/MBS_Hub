#!pip install boto3[crt]

import logging
import boto3
from botocore.exceptions import ClientError
import os

class DocumentBridge:
  bucket = None
  logger = None
  
  def init_app(self, app):
    self.bucket = app.config["AWS_S3_BUCKET"]
    self.logger = logging.getLogger(__name__)
  
  def save(self, file_name):
    object_name = os.path.basename(file_name)
    
    # Upload the file
    s3_client = boto3.client('s3')
    try:
      response = s3_client.upload_file(file_name, self.bucket, object_name)
      # response = s3_client.upload_file(file_name, app.config["AWS_S3_BUCKET"], object_name)
      self.logger.info(response)
    except ClientError as e:
      logging.error(e)
      return False
    return True
  
  def get(self, file_name):
    object_name = os.path.basename(file_name)
    s3 = boto3.client('s3')
    s3.download_file(self.bucket, object_name, file_name)
    # s3.download_file(app.config["AWS_S3_BUCKET"], object_name, file_name)
class MockDocumentBridge:
  def init_app(self, app): pass
  def save(self, file_name): pass
  def get(self, file_name): pass
