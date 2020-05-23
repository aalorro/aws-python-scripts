import boto3

ec2 = boto3.resource('ec2')

for instance in ec2.instances.all():
    print(
        "Id: {0}\nTag: {1}\nType: {2}\nPublic IPv4: {3}\nAMI: {4}\nState: {5}\n".format(
            instance.id, instance.tags, instance.instance_type, instance.public_ip_address, instance.image.id,
            instance.state
        )
    )