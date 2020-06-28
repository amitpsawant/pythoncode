import boto3
ec2 = boto3.resource('ec2')
if ec2 == None:
    print('Not found')
for instance in ec2.instances.all() :
    print('Instance ID is {} and Instance Type is {}'.format(instance.instance_id,instance.instance_type))
