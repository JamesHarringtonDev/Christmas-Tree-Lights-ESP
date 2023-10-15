import boto3

client = boto3.client('route53')

def updateRoute53Record(hosted_zone_id, record_name, my_ip):
    try:
        response = client.change_resource_record_sets(
            HostedZoneId=hosted_zone_id,
            ChangeBatch={
                "Comment": "Automatic DNS update",
                "Changes": [
                    {
                        "Action": "UPSERT",
                        "ResourceRecordSet": {
                            "Name": record_name,
                            "Type": "A",
                            "Region": "eu-west-2",
                            "TTL": 180,
                            "ResourceRecords": [
                                {
                                    "Value": my_ip
                                },
                            ],
                        }
                    },
                ]
            }
        )
    except Exception as e:
        print("What the fuck is this shit?")