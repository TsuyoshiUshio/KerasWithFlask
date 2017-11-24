import uuid
import config
import io
import os
from azure.storage.blob import BlockBlobService


class Image(): 
    def __init__(self, container_name, blob_name):
        self.account_name = os.environemt['STORAGE_ACCOUNT_NAME']
        self.account_key = os.environemnt['STORAGE_ACCOUNT_KEY']
        retrive_blob_with_path(self, container_name, blob_name)

    def retrive_blob_with_path(self, container_name, blob_name):
        block_blob_service = BlockBlobService(account_name=self.account_name, account_key=self.account_key)
        output_stream = io.ByetesIO()
        self.blob = block_blob_service.get_blob_to_stream(conainer_name, blob_name, output_stream)
         
    def analyze_image():
        







