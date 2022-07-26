import boto3
from trp import Document
import re

s3resource = boto3.resource('s3')

s3BucketName = "ocrbucket023200279992"

my_bucket = s3resource.Bucket(s3BucketName)

def OCR(s3BucketName, documentName, technique = "OCR"):
    try:
        if 0 == 0 : 
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

                #print(doc.pages[0].form)
                #with open('data/labels/form-vierge/form/label_passeport.txt', 'w') as f:
                    #f.write(doc.pages[0].form)

                for page in doc.pages:
                    # Print fields
                    print("Fields:")
                    i = 0
                    for field in page.form.fields:
                        i+=1

                print('data/'+folder[-3]+'/'+folder[-2]+'/output_'+folder[-1]+'.txt')
                with open('data/'+folder[-3]+'/'+folder[-2]+'/output_'+folder[-1]+'.txt', 'w') as f:
                    f.write(str(i))

                print('data/labels/'+folder[-3]+'/form/nb_key-value_'+folder[-2]+'.txt')
                with open('data/labels/'+folder[-3]+'/form/nb_key-value_'+folder[-2]+'.txt', 'r') as f:
                    nb = f.readline()


                key_value_rate = int((1 - (int(nb) - i)/int(nb))*10000)/100
                print('data/'+folder[-3]+'/'+folder[-2]+'/result_key-value_'+folder[-1]+'.txt')
                with open('data/'+folder[-3]+'/'+folder[-2]+'/result_key-value_'+folder[-1]+'.txt', 'w') as f:
                    f.write("Taux de Key-Value pairs : "+str(key_value_rate)+" %")
                    print("Taux de Key-Value pairs : "+str(key_value_rate)+" %")

                try:

                    print('data/'+'texte-manuscrit'+'/'+folder[-2]+'/output_'+folder[-1]+'.txt')
                    with open('data/'+'texte-manuscrit'+'/'+folder[-2]+'/output_'+folder[-1]+'.txt', 'w') as f:
                        for field in doc.pages[0].form.fields:
                            f.write(str(field.value)+'\n')

                    with open('data/'+'texte-manuscrit'+'/'+'constat'+'/output_'+'constatbleubrouillon.pdf'+'.txt', 'r') as f:
                        n = f.readlines()

                    with open('data/'+'texte-manuscrit'+'/'+'constat'+'/output_'+'constatbleubrouillon.pdf'+'.txt', 'w') as f:
                        for k in range(len(n)):
                            if n[k] != 'NOT_SELECTED\n':
                                if n[k] != 'SELECTED\n':
                                    if n[k] != 'None\n':
                                        f.write(n[k])

                except:
                    print("pb  ICR")

        

    except:
        print(" pb FORM")

    try:
        if technique == "OCR" :
            response = textract.detect_document_text(
                Document={
                    'S3Object': {
                        'Bucket': s3BucketName,
                        'Name': documentName
                }
                })
            
        doc = Document(response)

        with open('data/'+folder[-3]+'/'+folder[-2]+'/output_'+folder[-1]+'.txt', 'w') as f:
                f.write(doc.pages[0].text)

        #with open('data/labels/form-remplis/texte-brut/label_constat.txt', 'w') as f:
            #f.write(doc.pages[0].text)

    except:
        print("Pb OCR")

        
#OCR(s3BucketName, "data/form-remplis/passeport/passebleuok.pdf")