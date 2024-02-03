import boto3

client = boto3.client('s3')

response = client.select_object_content(
    Bucket='csv-bucket-to-ddb',
    Key='files/employees2.csv',
    Expression='Select * From s3object any_alias',
    ExpressionType='SQL',
    InputSerialization={'CSV': {'FileHeaderInfo': 'USE'}},
    OutputSerialization={'JSON': {}}
)

for i in response['Payload']:
    if 'Records' in i :
        print(i['Records']['Payload'].decode())