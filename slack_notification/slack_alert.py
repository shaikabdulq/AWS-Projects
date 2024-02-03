import requests
import json
import os
from base64 import b64decode
import boto3

ENCRYPTED = os.environ['SLACK_WEBHOOK']
DECRYPTED = boto3.client('kms').decrypt(
    CiphertextBlob=b64decode(ENCRYPTED),
    EncryptionContext={'LambdaFunctionName': os.environ['AWS_LAMBDA_FUNCTION_NAME']}
)['Plaintext'].decode('utf-8')

slack_web_hook = DECRYPTED

def send_slack(event, context):
    print(str(event))
    slack_message = {"text":"EC2 Instance Stopped"}
    resp = requests.post(slack_web_hook, data=json.dumps(slack_message))
    return resp.text
