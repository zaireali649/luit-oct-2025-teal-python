import boto3  # Import the AWS SDK for Python to interact with AWS services

s3 = boto3.client('s3')  # Create an S3 client to interact with Amazon S3

response = s3.list_buckets()  # Call the S3 API to list all buckets in the account

buckets = response["Buckets"]  # Extract the list of buckets from the API response

# Loop through each bucket and print its name
for bucket in buckets:
    print(bucket["Name"])
