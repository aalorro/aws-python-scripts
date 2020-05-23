import boto3, sys

ec2 = boto3.resource('ec2')

for id in sys.argv[1:]:
   instance = ec2.Instance(id)
   print(instance.terminate())