#! /bin/bash

FILENAME=ansible/hosts.ini
rm $FILENAME
touch $FILENAME
echo '[iscsi]' >> $FILENAME
yc compute instance list --format=json | \
    jq -r '.[]|select(.name | contains("iscsi")) | .network_interfaces[0]'.primary_v4_address.one_to_one_nat.address \
    >> $FILENAME
