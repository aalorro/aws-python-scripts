import boto3

print('')
user_input = input('What\'s the instance_id of the EC2 instance youo want to resize?: ')
print('')
user_input_size = input("What instance size to resize to?: ")

ec2 = boto3.client('ec2')

# Stop the instance
ec2.stop_instances(InstanceIds=[user_input])
waiter=ec2.get_waiter('instance_stopped')
waiter.wait(InstanceIds=[user_input])

# Change the instance type
ec2.modify_instance_attribute(InstanceId=user_input, Attribute='instanceType', Value=user_input_size)

# Start the instance
ec2.start_instances(InstanceIds=[user_input])

print('Instance ' + user_input + ' has been resized to ' + user_input_size)