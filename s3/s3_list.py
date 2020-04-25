import boto3
import click

session = boto3.Session(profile_name = 'santhu')
s3 = session.resource('s3')

@click.group()
def cli():
    "It deploys the s3 buckets"
    pass

@cli.command('list_buckets')
def list_buckets():
    "list all s3 buckets"
    for bucket in s3.buckets.all():
        print(bucket)


@cli.command('list_objects')
@click.argument('bucket')

def list_objects(bucket):
    "lists all objects in s3 bucket"
    for obj in s3.Bucket(bucket).objects.all():
        print(obj)


if __name__ == '__main__':
    cli()
