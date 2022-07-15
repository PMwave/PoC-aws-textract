import boto3
from trp import Document
from OCR import OCR
from WER import word_error_rate
s3BucketName = "ocrbucket379045149424"
s3client = boto3.client('s3')
s3resource = boto3.resource('s3')



my_bucket = s3resource.Bucket(s3BucketName)

for my_bucket_object in my_bucket.objects.all():
    print(my_bucket_object.key)
    path = str(my_bucket_object.key)
    folder = path.split("/")
    OCR(s3BucketName, my_bucket_object.key)

    with open('label_'+folder[-2]+'.txt', 'r') as file:
        data = file.read().replace('\n', ' ')



    with open('data/scan/'+folder[-2]+'/output_'+folder[-1]+'.txt', 'r') as file:
        result = file.read().replace('\n', ' ')

    distance, WER, WAcc = word_error_rate(data, result)
    print(f"Levenstein distance: {distance}")
    print(f"Word error rate: {WER}%")
    print(F"Word Accuracy: {WAcc}%")
    
    with open('data/scan/'+folder[-2]+'/result_'+folder[-1]+'.txt', 'w') as f2:
        f2.write(f"Levenstein distance: {distance}")
        f2.write(f"Word error rate: {WER}%")
        f2.write(F"Word Accuracy: {WAcc}%")