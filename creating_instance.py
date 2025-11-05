from helpers import *  # Import helper functions (e.g., create_ubuntu_instance, get_ec2_client, etc.)

def create_instances(ec2_client, ami_type: str = "ubuntu", ami_amount: int = 1) -> None:
    """
    Create one or more EC2 instances based on the specified AMI type.

    Args:
        ec2_client: The EC2 client object used to interact with AWS EC2.
        ami_type (str): The type of AMI to launch. Supported values: 
                        "ubuntu", "linux2023", "linux2". Defaults to "ubuntu".
        ami_amount (int): The number of instances to create. Defaults to 1.

    Returns:
        None
    """
    # Normalize the AMI type for comparison (lowercase, no spaces)
    clean_ami_type = ami_type.lower().strip().replace(" ", "")

    # Loop to create the desired number of instances
    for i in range(ami_amount):
        if clean_ami_type == "ubuntu":
            create_ubuntu_instance(ec2_client)  # Launch Ubuntu instance
            print("Created Ubuntu")
        elif clean_ami_type == "linux2023":
            create_amazon_linux_2023_instance(ec2_client)  # Launch Amazon Linux 2023 instance
            print("Created Linux 2023")
        elif clean_ami_type == "linux2":
            create_amazon_linux_2_instance(ec2_client)  # Launch Amazon Linux 2 instance
            print("Created Linux 2")
        else:
            # Handle unsupported AMI types
            print("Unsupported AMI Type")


if __name__ == "__main__":
    # Initialize EC2 client
    ec2 = get_ec2_client()

    # Test various AMI type inputs and instance counts
    create_instances(ec2)
    create_instances(ec2, "Ubuntu")
    create_instances(ec2, "Linux 2")
    create_instances(ec2, "ubuntu")
    create_instances(ec2, "ubuNtu")
    create_instances(ec2, "Linux 2023  ")
    create_instances(ec2, "  Linux 2023")
    create_instances(ec2, "Linux   2023")
    create_instances(ec2, "Linux 2", 3)
    create_instances(ec2_client=ec2, ami_type="Linux 2", ami_amount=3)
    create_instances(ec2_client=ec2, ami_amount=2)
