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

To Run 

`pipenv run "python ec2/ec2_stop.py <tag-name>"
