# Import boto3 library
import boto3

# Initialize boto3 s3 client
s3 = boto3.client("s3")

# Define variable for a region
REGION = "us-east-1"

# Create empty list
BUCKET_LIST = []

# print(type(s3))
# print(type(boto3))
# print(dir(boto3))
# print(dir(boto3.s3))

# List S3 buckets and save as "response"
response = s3.list_buckets()

# Iterate thru response list and print bucketname
for bucket in response["Buckets"]:
    BUCKET_LIST.append(bucket["Name"])
    
for bucket in BUCKET_LIST:
    bucket_location = s3.get_bucket_location(Bucket=bucket)
    print(bucket_location)
