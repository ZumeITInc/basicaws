import boto3
import click

session = boto3.Session(profile_name='santhu')
ec2 = session.resource('ec2')
@click.group()
def instances():
    """Commands for instances"""

@instances.command('list')
@click.option('--project',default=None,
              help="Only instances for project (tag Project:Name)")
def list_instances(project):
    "list the ec2 instances"
    instances= []

    if project :
        filters =[{'Name':'tag:Name', 'Value':[project]}]
        instances = ec2.instances.filter(Filters=filters)
    else:
        instances = ec2.instances.all()

    for i in instances:
        tags ={t['Key']: t['Value']for t in i.tags or []}
        print(', '.join((
            i.id,
            i.instance_type,
            i.placement['AvailabilityZone'],
            i.state['Name'],
            i.public_dns_name,
            tags.get('Name', '<no project>')
        )))

@click.group('volumes')
def volumes():
    "commands for volumes"

@volumes.command('list')
@click.option('--project',default=None,
              help="Only volumes for project (tag Project:Name)")
def list_volumes():
    for i in instances:
        for v in i.voumes.all():
            print(', '.join((
                v.id,
                i.id,
                v.state,
                str(v.size) + "Gib",
                v.encrypted and "Encrypted" or "Not Encrypted"
            )))

    return

if __name__ ==' __main__':
    list_instances()
    list_volumes()