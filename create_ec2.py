import boto3
# create new ec2 instance
ec2 = boto3.resource('ec2')

instance = ec2.create_instances(
    ImageId = 'ami-0f7919c33c90f5b58',
    MinCount = 1,
    MaxCount = 1,
    SecurityGroupIds = ['sg-086d7dae46341023c'],
    InstanceType = 't2.small',
    KeyName = 'alorro2020',
    SubnetId = 'subnet-40e1b928')

print (instance[0].id)