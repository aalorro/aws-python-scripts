import boto3

ec2 = boto3.resource('ec2')

instance = ec2.create_instances(
    ImageId = 'ami-0f7919c33c90f5b58',
    MinCount = 1,
    MaxCount = 1,
    InstanceType = 't2.micro',
    KeyName = 'alorro2020',
    SubnetId = 'subnet-40e1b928')

print (instance[0].id)