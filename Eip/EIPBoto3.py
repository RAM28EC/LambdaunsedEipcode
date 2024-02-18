import boto3
def lambda_handler(event, context):
    client = boto3.client('ec2')
    addresses = client.describe_addresses()['Addresses']
    for eip in addresses:
        if ('AssociationId' not in eip) and ('NetworkInterfaceId' not in eip):
            print(eip['PublicIp'] + " is unused, releasing")
            client.release_address(AllocationId=eip['AllocationId'])
        else:
            print(eip['PublicIp'] + "is used, not releasing")
    return {
        'statusCode': 200,
        'body': 'Unused Elastic IPs deleted successfully!'
    }
    
    
    


