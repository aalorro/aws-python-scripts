import boto3

user_input = input('Instance_id to start: ')

ec2 = boto3.resource('ec2')
ec2.Instance(user_input).start()

print('Starting instance ' + user_input)