from ip import getCurrentIpV4
from route53 import updateRoute53Record


### get the current IP
current_ip = getCurrentIpV4()
hosted_zone_id = "Z08955742YM4609U4U7BM"
record_name = "dev.jamesharrington.co.uk"
### check if it's in SQlite, and if so, up
ip_needs_saving = True

### Work some magic to update the route53
if ip_needs_saving:
    updateRoute53Record(
        hosted_zone_id,
        record_name,
        current_ip
    )

    print(f'update record for: hostedZoneId: {hosted_zone_id} \n record_name {record_name} \n current_ip: {current_ip}')

###