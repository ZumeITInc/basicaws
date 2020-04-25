# basicaws
Automating AWS with Python

Demo project to manage ec2 instances

##About
This project is a demo, and uses boto3 to manage AWS EC2 instances.

##Configuring

Santhu uses the configuration file created by the AWS cli. 
e.g.

`aws configure --profile santhu`

##Running

`pipenv run "python ec2/ec2_list.py"`

##Running

`pipenv run "python ec2/ec2_stop.py <command> <--tag-name>"`

*command* is list, start, and  stop
*tag-name* is optional

## Running

`pipenv run "python ec2/ec2_list_volumes.py <command> <--tag-name">`

*command* is list
*tag-name* is optional

##Running

`pipenv run "python ec2/ec2_list_shnapshots.py <command> <--tag-name>"`

*command* is list, and create_snapshots
*tag-name* is optional

##Running

`pipenv run "python s3/s3_list.py" <command> <options>`

*command* is list_buckets or list_objects
*options* is bucket name to display objects