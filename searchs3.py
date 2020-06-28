import boto3

client = boto3.client('s3')
bucketlist = client.list_buckets()
for content in bucketlist['Buckets']:
    if "eagles" in content['Name'] and "alblog" not in content['Name'] and "terraform" not in content['Name']:
        bucketname = content['Name']
        print ("Bucket Name : {}".format(bucketname))

response = client.list_objects_v2(Bucket=bucketname, Prefix='recordings-screen' )

print ('\nList of files')
for content in response['Contents']:
    if "77_3bb31d36-7b21-466e-bca0-4a22cf554e82_892_36209.mp4" in content['Key']:
        print(content['Key'])
    if "77_21e15a6f-249d-43f7-8e11-205d6878c898_889_36209.mp4" in content['Key']:
        print(content['Key'])
