import boto3

user_input = input('Instance_id to stop: ')

ec2 = boto3.resource('ec2')
ec2.Instance(user_input).stop()

print('Stopping instance ' + user_input)