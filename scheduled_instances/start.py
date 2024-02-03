import boto3
ec2_client = boto3.client('ec2')
ec2 = boto3.resource('ec2')

def lambda_handler(event, context):
    response = ec2_client.describe_instances(Filters=[
        {
            'Name': 'tag:Type',
            'Values': [
                'Scheduled',
            ]
        }
    ])
    instance_ids = []
    for list in response['Reservations']:
        for instance in list['Instances']:
            id = instance['InstanceId']
            instance_ids.append(id)
    
    for id in instance_ids:
        instance = ec2.Instance(id)
        instance.start()
        
    return "success"
