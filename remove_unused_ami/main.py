import boto3

client = boto3.client('ec2',region_name='ap-south-1')
response = client.describe_instances()
used_ami = []
for reservation in response['Reservations']:
    for instance in reservation['Instances']:
        used_ami.append(instance['ImageId'])

def remove_duplicates(ami_list):
    unique_list = []
    for ami in ami_list:
        if ami not in unique_list:
            unique_list.append(ami)
    return unique_list

used_ami = remove_duplicates(used_ami)

response = client.describe_images(Owners=['self'])

owned_ami = []
for image in response['Images']:
    owned_ami.append(image['ImageId'])

for ami in owned_ami:
    if ami not in used_ami:
        client.deregister_image(
            ImageId=ami
        )
        print(f'Deregistered ami: {ami}')
