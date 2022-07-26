import boto3
from trp import Document
from OCR import OCR
from WER import word_error_rate
s3BucketName = "ocrbucket023200279992"
s3client = boto3.client('s3')
s3resource = boto3.resource('s3')



my_bucket = s3resource.Bucket(s3BucketName)

for my_bucket_object in my_bucket.objects.all():
    print(my_bucket_object.key)
    path = str(my_bucket_object.key)
    folder = path.split("/")
    print("--------------OCR--------------")
    OCR(s3BucketName, my_bucket_object.key, technique = "OCR")

    with open('data/labels/'+folder[-3]+'/texte-brut/label_'+folder[-2]+'.txt', 'r') as file:
        data = file.read().replace('\n', ' ')


    with open('data/'+folder[-3]+'/'+folder[-2]+'/output_'+folder[-1]+'.txt', 'r') as file:
        result = file.read().replace('\n', ' ')

    distance, WER, WAcc = word_error_rate(data, result)
    print(f"Levenstein distance: {distance}")
    print(f"Word error rate: {WER}%")
    print(F"Word Accuracy: {WAcc}%")
    
    with open('data/'+folder[-3]+'/'+folder[-2]+'/result_texte-brut_'+folder[-1]+'.txt', 'w') as f2:
        f2.write(f"Levenstein distance: {distance}"+"\n")
        f2.write(f"Word error rate: {WER} %"+"\n")
        f2.write(F"Word Accuracy: {WAcc} %"+"\n")

    print("--------------FORM--------------")
    OCR(s3BucketName, my_bucket_object.key, technique = "FORM")

    if folder[-3] == 'form-remplis' :
        print("--------------ICR--------------")

        with open('data/labels/'+'texte-manuscrit'+'/label_'+folder[-2]+'.txt', 'r') as file:
            data = file.read().replace('\n', ' ')


        with open('data/'+'texte-manuscrit'+'/'+folder[-2]+'/output_'+folder[-1]+'.txt', 'r') as file:
            result = file.read().replace('\n', ' ')

        distance, WER, WAcc = word_error_rate(data, result)
        print(f"Levenstein distance: {distance}")
        print(f"Word error rate: {WER}%")
        print(F"Word Accuracy: {WAcc}%")
        
        with open('data/'+'texte-manuscrit'+'/'+folder[-2]+'/result_texte-brut_'+folder[-1]+'.txt', 'w') as f2:
            f2.write(f"Levenstein distance: {distance}"+"\n")
            f2.write(f"Word error rate: {WER} %"+"\n")
            f2.write(F"Word Accuracy: {WAcc} %"+"\n")