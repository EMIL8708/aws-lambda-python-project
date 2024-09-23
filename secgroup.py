import boto3 
import json

def lambda_handler(event, context):
    REGION = "es-east-1"

    ec2 = boto3.client('ec2', region_name=REGION)

    response = ec2.describe_security_groups()

    unused_secgroups = []

    # Find sec groups
    for items in response['SecurityGroups']:
        unused_secgroups.append(items['GroupId'])

    # delete sec groups
    for sg in unused_secgroups:
        try:
            ec2.delete_security_group(GroupId=sg)
            print("Deleted Security Group %s" % sg)
        except:
            print("Could not delete Security Group %s" % sg)
