import boto3

client = boto3.client('route53')

def updateRoute53Record(source, target):
    try:
        response = client.change_resource_record_sets(
        HostedZoneId='Z08955742YM4609U4U7BM',
        ChangeBatch= {
            'Comment': 'add %s -> %s' % (source, target),
            'Changes': [
                {
                    'Action': 'UPSERT',
                    'ResourceRecordSet': {
                        'Name': source,
                        'Type': 'CNAME',
                        'TTL': 300,
                        'ResourceRecords': [{'Value': target}]
                }   
            }]
        })
    except Exception as e:
        print("What the fuck is this shit?")