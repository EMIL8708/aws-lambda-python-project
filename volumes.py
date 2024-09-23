import json
import boto3 

def lambda_handler(event, context):
    REGION = 'es-east-1'

    ec2 = boto3.client('ec2', region_name=REGION)

    available_volumes = []

    paginator = ec2.get_paginator('describe_volumes')

    # find volumes 
    for items in paginator.paginate(Filters=[{'Name': 'status', 'Values': ['available']}]):
        for volume in items['Volumes']:
            available_volumes.append(volume['VolumeId'])

    # Create a snapshot of volumes
    for volume in available_volumes:
        snapshot = ec2.create_snapshot(
            VolumeId=volume,
            Description='Snapshot of volume ' + volume
        )
        print('Snapshot created for volume', volume)
        print(snapshot['SnapshotId'])
        print('-----------------')

    # Delete volumes
    for volume in available_volumes:
        ec2.delete_volume(VolumeId=volume)
        print('The volume %s has been deleted' % volume)
