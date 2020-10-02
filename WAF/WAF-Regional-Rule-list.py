import boto3

def set_boto3_client(service_name, region):
    """set boto3 service and region"""

    client = boto3.client(
        service_name=service_name,
        region_name=region)

    return client


def list_webacl_rules(service_name='waf-regional', region):
    """
    List WebAcl rules and IP address for desired WebAcl.
    Provide WebAcl id to list for rules.
    """

    client = set_boto3_client(service_name=service_name, region=region)

    ip_sets = client.list_ip_sets()
    ip_address = ip_sets['IPSets']

    for ipset in ip_address:
        print(f"Rule Name: {ipset['Name']}")
        result = client.get_ip_set(IPSetId=ipset['IPSetId'])
        if descriptors := result['IPSet']['IPSetDescriptors']:
            for descriptor in descriptors:
                print(
                    f"{descriptor['Type']}: {descriptor['Value']}")
        else:
            print("**Empty**")

# invoke function
list_webacl_rules(region='eu-west-1')
