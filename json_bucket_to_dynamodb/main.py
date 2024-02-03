import json
import boto3
s3_client = boto3.client('s3')
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('employees')

def lambda_handler(event, context):
    bucket = event['Records'][0]["s3"]['bucket']['name']
    key = event['Records'][0]["s3"]['object']['key']
    resp = s3_client.get_object(Bucket=bucket,Key=key)
    json_body = resp['Body'].read()
    json_data = json.loads(json_body)
    table.put_item(Item=json_data)
