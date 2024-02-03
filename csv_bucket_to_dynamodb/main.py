import json
import boto3
s3_client = boto3.client('s3')
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('employees')

bucket = event['Records'][0]["s3"]['bucket']['name']
key = event['Records'][0]["s3"]['object']['key']
resp = s3_client.get_object(Bucket=bucket,Key=key)
list = (resp['Body'].read().decode('utf-8')).split('\n')
print(list)
for item in list:
    # print(item)
    data = (item.strip()).split(',')
    # print(data)
    table.put_item(Item={
        'id':data[0],
        'name':data[1],
        'location':data[2]
    })
