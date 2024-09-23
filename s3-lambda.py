# import boto3 library
import boto3 
import json

def lambda_handler(event, context):
    # Initialize boto3 s3 client 
    s3 = boto3.client("s3")

    # Define a variable for a region
    REGION = "us-east-1"

    # Create empty list
    BUCKET_LIST = []

    TAGS = {
        'TagSet': [
            {
                'Key': 'envi',
                'Value': 'dev'
            },
            {
                'Key': 'managedBy',
                'Value': 'terraform'
            },
            {
                'Key': 'python',
                'Value': 'project'
 },
{
                'Key': 'month',
                'Value': 'september'
            },
        ]
    }

    # List S3 buckets and save as "response"
    response = s3.list_buckets()

    # iterate thru response list and print bucket name
    for bucket in response["Buckets"]:
        BUCKET_LIST.append(bucket["Name"])

    for bucket in BUCKET_LIST:
        # Find bucket location
        bucket_location = s3.get_bucket_location(Bucket=bucket) 
        bucket_region = bucket_location["LocationConstraint"]

        # if the bucket is in the region
        if bucket_region == REGION:
            # print to the screens
            print("The bucket %s is located in %s" % (bucket, bucket_region))
            # add tags
            response = s3.put_bucket_tagging(Bucket=bucket,Tagging=TAGS)
            print("The following buckets %s are tagged" % bucket)
