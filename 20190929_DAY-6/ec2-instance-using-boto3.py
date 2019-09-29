import boto3 

ec2 = boto3.client('ec2')

response = ec2.run_instances(
    ImageId='ami-009110a2bf8d7dd0a',
    InstanceType='t2.micro',
    KeyName='keshavkummari_aws',
    MinCount=1,
    MaxCount=1
)
print(response)
