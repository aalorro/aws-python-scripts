import boto3

user_input = input('What\'s the instance_id of the EC2 instance youo want to start?: ')

ec2 = boto3.resource('ec2')
ec2.Instance(user_input).start()

print('Starting instance ' + user_input)