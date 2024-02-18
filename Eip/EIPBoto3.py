import boto3
client = boto3.client('ec2')
addresses = client.describe_addresses()['Addresses']
for eip in addresses:
    if ('AssociationId' not in eip) and ('NetworkInterfaceId' not in eip):
        print(eip['PublicIp'] + " is unused, releasing")
        client.release_address(AllocationId=eip['AllocationId'])
    else:
        print(eip['PublicIp'] + "is used, not releasing")    
    
    


