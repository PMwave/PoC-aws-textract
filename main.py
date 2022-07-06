import boto3
from trp import Document
from OCR import OCR

s3BucketName = "ocrbucket379045149424"
s3client = boto3.client('s3')
s3resource = boto3.resource('s3')



OCR(s3BucketName, "data/scan/constat/Scan12.pdf")