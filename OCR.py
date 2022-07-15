import boto3
from trp import Document



def OCR(s3BucketName, documentName, technique = "OCR"):
    
    folder = documentName.split("/")
    print(folder)
    textract = boto3.client('textract', region_name='eu-west-1')
    if technique == "FORM" :
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

    if technique == "OCR" :
        response = textract.detect_document_text(
            Document={
                'S3Object': {
                    'Bucket': s3BucketName,
                    'Name': documentName
                }
            })
        
        doc = Document(response)

        with open('data/scan/'+folder[-2]+'/output_'+folder[-1]+'.txt', 'w') as f:
            f.write(doc.pages[0].text)

        
