import boto3  # Import the AWS SDK for Python to interact with AWS services

# Create a low-level EC2 client to interact with the Amazon EC2 service
vpc_client = boto3.client('ec2')

# Retrieve information about all VPCs in the current AWS account and region
response = vpc_client.describe_vpcs()

# Extract the list of VPCs from the API response
vpcs = response['Vpcs']

# Loop through each VPC and print its unique VPC ID
for vpc in vpcs:
    print(vpc['VpcId'])
