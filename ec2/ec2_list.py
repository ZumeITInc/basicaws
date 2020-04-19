<<<<<<< HEAD
import boto3
import click

session = boto3.Session(profile_name='santhu')
ec2 = session.resource('ec2')

@click.command()
def list_instances():
    "list the ec2 instances"
    for i in ec2.instances.all():
        print(', '.join((
            i.id,
            i.instance_type,
            i.placement['AvailabilityZone'],
            i.state['Name'],
            i.public_dns_name)))
    return

if __name__ ==' __main__':
=======
import boto3
import click

session = boto3.Session(profile_name='santhu')
ec2 = session.resource('ec2')

@click.command()
def list_instances():
    "list the ec2 instances"
    for i in ec2.instances.all():
        print(', '.join((
            i.id,
            i.instance_type,
            i.placement['AvailabilityZone'],
            i.state['Name'],
            i.public_dns_name)))
    return

if __name__ ==' __main__':
>>>>>>> f94bb4c3ab2f02b4ee0d10ab486abd5d9dbc11b9
    list_instances()