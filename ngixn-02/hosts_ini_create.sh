#! /bin/bash

FILENAME=ansible/hosts.ini
touch $FILENAME
echo '[loadbalanser]' >> $FILENAME
yc compute instance list --format=json | \
    jq -r '.[]|select(.name | contains("nginx")) | .network_interfaces[0]'.primary_v4_address.one_to_one_nat.address \
    >> $FILENAME
echo '[webserver]' >> $FILENAME
yc compute instance list --format=json | \
    jq -r '.[]|select(.name | contains("web")) | .network_interfaces[0]'.primary_v4_address.one_to_one_nat.address \
    >> $FILENAME