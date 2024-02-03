import boto3
from datetime import date
ec2_client = boto3.client('ec2')
sns_client = boto3.client('sns')
volumes = ec2_client.describe_volumes()
sns_arn = "ENTER_SNS_ARN" #Replace with your SNS ARN

unused_vols = []
for volume in volumes['Volumes']:
    unused_vols.append(volume['VolumeId'])

#Send email
current_date = date.today()
email_body = f"##### Unused AWS Volumes as on {current_date} #####\n\n"

for volume in unused_vols:
    email_body = email_body + f'Volume Id: {volume}\n'

sns_client.publish(
    TopicArn = sns_arn,
    Subject = "Unused AWS Volumes",
    Message = email_body,
)