import boto3
from trp import Document





def OCR(s3BucketName, documentName):
    textract = boto3.client('textract', region_name='eu-west-1')

    response = textract.analyze_document(
        Document={
            'S3Object': {
                'Bucket': s3BucketName,
                'Name': documentName
            }
        },
        FeatureTypes=["FORMS"])
    
    doc = Document(response)

    for page in doc.pages:
    # Print fields
        print("Fields:")
        for field in page.form.fields:
            print("Key: {}, Value: {}".format(field.key, field.value))
            print(field)