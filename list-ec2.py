import boto3
from termcolor import colored

ec2 = boto3.resource('ec2')

for instance in ec2.instances.all():
    print(
        "Id: {0}\nTags: {1}\nType: {2}\nPublic IPv4: {3}\nPrivate IP: {4}\nState: {5}\nSecurity Groups: {6}".format(
            colored(instance.id, 'yellow'), instance.tags, instance.instance_type, instance.public_ip_address, instance.private_ip_address,
            instance.state, instance.security_groups
        )
    )
    print(
        "Launched: {0}\nPriv DNS: {1}\nPublic DNS: {2}\nVPC: {3}\nSubnet ID: {4}\nAMI: {5}\nKey Pair: {6}\n\n".format(
            instance.launch_time, instance.private_dns_name, instance.public_dns_name, instance.vpc, instance.subnet_id,
            instance.image_id, instance.key_pair
        )
    )