import boto3

region = 'us-east-2'
instances = ['i-0b8e04c02e8856c5a'] # you may input as many instances in the list

ec1 = boto3.client('ec2', region_name=region)

def lambda_handler(event, context):
    ec1.stop_instances(InstanceIds=instances)
    print('stopped your instances: ' + str(instances))