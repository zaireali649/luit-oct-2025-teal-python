from typing import Any, Dict, List
from helpers import *  # Importing helper functions for AWS client creation and resource listing


def print_bucket_names(s3_client: Any) -> None:
    """
    Prints the names of all S3 buckets available to the provided client.

    Args:
        s3_client (Any): A boto3 S3 client object used to interact with AWS S3.

    Example:
        >>> s3 = get_s3_client()
        >>> print_bucket_names(s3)
        bucket-1
        bucket-2
    """
    # Retrieve list of bucket names from helper function
    bucket_names: List[str] = list_buckets(s3_client)

    # "\n".join(bucket_names) # String manipulation to get the same result
    # Iterate through the bucket names and print each one
    for bucket_name in bucket_names:
        print(bucket_name)


def print_instance_ids(ec2_client: Any) -> None:
    """
    Prints the instance IDs of all EC2 instances accessible to the provided client.

    Args:
        ec2_client (Any): A boto3 EC2 client object used to interact with AWS EC2.

    Example:
        >>> ec2 = get_ec2_client()
        >>> print_instance_ids(ec2)
        i-0abcd1234ef567890
        i-0fedcba9876543210
    """
    # Retrieve EC2 instance details from helper function
    instances: List[Dict[str, Any]] = describe_instances(ec2_client)

    # Extract instance IDs from the response
    instance_ids = []
    for instance in instances:
        instance_ids.append(instance["InstanceId"])

    # Print each instance ID
    for instance_id in instance_ids:
        print(instance_id)


if __name__ == "__main__":
    """
    Script entry point:
    - Creates AWS EC2 and S3 clients.
    - Prints all S3 bucket names and EC2 instance IDs.
    """
    # Initialize AWS clients
    ec2_client: Any = get_ec2_client()
    s3_client: Any = get_s3_client()

    # Display available S3 buckets
    print_bucket_names(s3_client)

    # Display EC2 instance IDs
    print_instance_ids(ec2_client)
