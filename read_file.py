import boto3
from trp import Document
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
import os
import glob

s3BucketName = "ocrbucket379045149424"
s3client = boto3.client('s3')
s3resource = boto3.resource('s3')

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
    for file in files :
        s3client.upload_file(
        Filename=file,
        Bucket=s3BucketName,
        Key=file.split('../')[-1].replace("\\", "/"),
        )

    print('check')


#upload_files("../../../data/scan")