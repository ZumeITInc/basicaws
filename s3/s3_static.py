import boto3
import click

session = boto3.Session(profile_name = 'santhu')
s3 = session.resource('s3')

@click.group()
def cli():
    "It creates the S3 bucket and configure the Static Website"
    pass

@cli.command('create_bucket')
def create_bucket():
    "It creates an S3 bucket"
    name = input('Enter bucket name: ')
    new_bucket = s3.create_bucket(Bucket=name, CreateBucketConfiguration={'LocationConstraint' : 'ap-south-1'})
    print("Creating S3", name, " bucket")
    print(new_bucket)

@cli.command('upload_file')
def upload_file(new_bucket=None):
    "It uploads a file to new bucket"
    s3.Object(new_bucket, './index.html').upload_file('/tmp/index.html')
    print("uploading...")

    return

if __name__ == '__main__':
    cli()
