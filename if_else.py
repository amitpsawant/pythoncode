import boto3
client = boto3.client('ec2')
##resp = client.run_instances(ImageId='ami-04b2519c83e2a7ea5',
##                            InstanceType='t2.micro',
##                            MinCount=1,
##                            MaxCount=1)
##for instance in resp['Instances']:
##    print(instance['InstanceId'])
##

##
##response = client.stop_instances(
##    InstanceIds=[
##        'i-021cb6dc3cc22a021'
##    ]
##)

response = client.terminate_instances(
    InstanceIds=[
        'i-021cb6dc3cc22a021'
    ]
)
