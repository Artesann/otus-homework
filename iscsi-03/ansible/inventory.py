#!/usr/bin/env python3

import requests
import json
import subprocess
import argparse


def get_iqn(ip):
    out = subprocess.check_output(["ssh", "-o", "StrictHostKeyChecking=no", ip, "echo", "InitiatorName=`sudo /sbin/iscsi-iname`", "|", "sudo", "tee", "/etc/iscsi/initiatorname.iscsi"])
    iqn = subprocess.check_output(["ssh", "-o", "StrictHostKeyChecking=no", ip, "sudo", "cat", "/etc/iscsi/initiatorname.iscsi"])
    return str(iqn).split('\\n')[-2].split('=')[1]


def get_hostvars():
    vars = {}
## default 
    for instance in responce['instances']:
        vars[instance['name']] = {"ansible_host": 
            instance['networkInterfaces'][0]['primaryV4Address']['oneToOneNat']['address']}
    
## custom
    
    for key, group in get_groups().items():
        if key == "iscsi":
            for host in group['hosts']:
                vars[host]['iqns'] = []
                for initiator_host in get_groups()['initiator']['hosts']:
                    vars[host]['iqns'].append(get_iqn(vars[initiator_host]['ansible_host']))
    return vars


def get_groups():
    all = {}
    for group in host_groups:
        hosts = []
        for instance in responce['instances']:
            if group in instance['name']:
                hosts.append(instance['name'])
        all[group]= {"hosts": hosts}
    return all

def get_all_vars():
    vars = {}
    vars["target_iqn"] = "iqn.2022-11.pepe.arty:storage.target00"
    for instance in responce['instances']:
        if instance['name'] == "iscsi":
            vars['target_ip'] = instance['networkInterfaces'][0]['primaryV4Address']['address']
    return vars
        
    

def get_list():
    result_inventory = inventory | get_groups()
    result_inventory['_meta']['hostvars'] = get_hostvars()
    result_inventory['all']['children'] = host_groups 
    result_inventory['all']['vars'] = get_all_vars()
    return result_inventory


parser = argparse.ArgumentParser()
parser.add_argument(
    '--pretty',
    action='store_true',
    default=False,
    help="Pretty print JSON"
)
parser.add_argument(
    "--list",
    action='store',  # also better use store_true
    nargs="*",
    default="dummy",
    help="Show JSON of all managed hosts"
)
parser.add_argument(
    "--host",
    action='store',
    help="Display vars related to the host"
)
args = parser.parse_args()


inventory = {
  "_meta": {
    "hostvars": {}
  },
  "all": {
    "children": [],
    "vars": {}
  }
}

token = open("token").read()
folder_id = "b1gaf9l1lrdtb72755nd"
host_groups = ["iscsi", "initiator"] # instance must contain in name one of it


r = requests.get("https://compute.api.cloud.yandex.net/compute/v1/instances?folderId=" + folder_id, 
    headers={"Authorization": "Bearer " + token})

if r.status_code != 200:
    raise Exception("HTTP responce code from yc is " + str(r.status_code))

responce = json.loads(r.text)
# Print output will be parsed via ansible as inventory (like a file).
if args.host:
    print(json.dumps(get_hostvars()[args.host], indent=args.pretty))
elif len(args.list) >= 0:
    print(json.dumps(get_list(), indent=args.pretty))
else:
    raise ValueError("Expecting either --host $HOSTNAME or --list")