# Christmas-Tree-Lights-ESP

## Update Route-53

Python script which is which:

1. Gets the current IPV4 address
1. Checks if we already have one stored in a local SQLite database
    - If not, updates the route-53 record for to point the specified domain to this IP address
    - If it does, checks if the value has changed. If it has, update the IP route-53 record then update the database record with the new latest IP address. Otherwise, don't do anything
