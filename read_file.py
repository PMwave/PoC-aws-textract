import boto3
from trp import Document

import os
import glob

s3BucketName = "ocrbucket023200279992"
s3client = boto3.client('s3', region_name='eu-west-1')
s3resource = boto3.resource('s3', region_name='eu-west-1')

def delete_bucket_content():
   
    my_bucket = s3resource.Bucket(s3BucketName)

    for my_bucket_object in my_bucket.objects.all():
        print(my_bucket_object.key)
        s3client.delete_object(Bucket = s3BucketName,Key = my_bucket_object.key)

def list_files(root):

    files = glob.glob(os.path.join(root, "**/*.pdf"), recursive=True)

    return(files)

def upload_files(root):
    files = list_files(root)
    print(files)
    for file in files :
        s3client.upload_file(
        Filename=file,
        Bucket=s3BucketName,
        Key=file.split('../')[-1].replace("\\", "/"),
        )

    print('check')

delete_bucket_content()
upload_files("../data/form-remplis")
upload_files("../data/form-vierge")