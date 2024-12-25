import boto3

def extract_text_from_pdf(file_path):
    textract_client = boto3.client('textract')

    with open(file_path, 'rb') as file:
        response = textract_client.analyze_document(
            Document={'Bytes': file.read()},
            FeatureTypes=['FORMS', 'TABLES']
        )

    text = ''
    for block in response['Blocks']:
        if block['BlockType'] == 'LINE':
            text += block['Text'] + '\n'
    
    return text
