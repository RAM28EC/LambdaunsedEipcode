import json

import boto3
def lambda_handler(event, context):
    client = boto3.client('ec2')
     # Get list of all AWS regions
    regions = [region['RegionName'] for region in client.describe_regions()['Regions']]
    print("All regions:", regions)
    # Iterate through each region
    for region in regions:
        print(f"Cleaning up unused Elastic IPs in region: {region}")
        ec2_client_region = boto3.client('ec2', region_name=region)
        addresses = ec2_client_region.describe_addresses()['Addresses']
        for eip in addresses:
            if ('AssociationId' not in eip) and ('NetworkInterfaceId' not in eip):
                print(eip['PublicIp'] + " is unused, releasing")
                ec2_client_region.release_address(AllocationId=eip['AllocationId'])
            else:
                print(eip['PublicIp'] + "is used, not releasing")
    return {
        'statusCode': 200,
        'body': 'Unused Elastic IPs deleted successfully!'
    }
