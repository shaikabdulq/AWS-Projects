import boto3

# To get list of running EC2 Instances
ec2 = boto3.resource('ec2')
client = boto3.client('ec2')
instances = ec2.instances.filter(Filters=[
        {
            'Name': 'instance-state-name',
            'Values': [
                'running',
            ]
        }
    ])

# To create images and get image_ids list
image_ids = []
for instance in instances:
    image = instance.create_image(Name='test-image'+instance.instance_id)
    image_id = image.image_id
    image_ids.append(image_id)

# To wait till the AMI gets generated
waiter = client.get_waiter('image_available')
waiter.wait(
    ImageIds=image_ids
)

# To copy AMI to another region
client = boto3.client('ec2',region_name='us-east-1')
for image_id in image_ids:
    response = client.copy_image(
        Name='Copy-of-test-image'+image_id,
        SourceImageId=image_id,
        SourceRegion='ap-south-1'
    )



