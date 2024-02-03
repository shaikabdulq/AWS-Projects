import boto3

client = boto3.client('sns')
sns_arn = 'ENTER_SNS_ARN' # Replace with your SNS ARN

client.publish(
    TopicArn=sns_arn,
    Message='Production Instance Stopped. Kindly look into the issue',
    Subject='Production Instance Stopped'
        )
