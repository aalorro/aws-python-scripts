import boto3

user_input = input('Instance_id to reboot: ')

ec2 = boto3.resource('ec2')
ec2.Instance(user_input).reboot()

print('Rebooting instance ' + user_input)