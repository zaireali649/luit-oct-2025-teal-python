from helpers import * 

def create_instances(ec2_client, ami_type="ubuntu", ami_amount=1):
    clean_ami_type = ami_type.lower().strip().replace(" ", "")
    for i in range(ami_amount):
        if clean_ami_type == "ubuntu":
            create_ubuntu_instance(ec2_client)
            print("Created Ubuntu")
        elif clean_ami_type == "linux2023":
            create_amazon_linux_2023_instance(ec2_client)
            print("Created Linux 2023")
        elif clean_ami_type == "linux2":
            create_amazon_linux_2_instance(ec2_client)
            print("Created Linux 2")
        else:
            print("Unsupported AMI Type")
    
if __name__ == "__main__":
    ec2 = get_ec2_client()
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