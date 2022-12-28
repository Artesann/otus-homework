#!/usr/bin/env python3

import requests
import json
import argparse

def get_hostvars():
## default 
    vars = {}
    for instance in responce['instances']:
        vars[instance['name']] = {"ansible_host": 
            instance['networkInterfaces'][0]['primaryV4Address']['oneToOneNat']['address']}
    
## custom
    return vars


def get_groups():
    all = {}
    for instance in responce['instances']:
        if instance['name'].split('-')[0] in all:
            all[instance['name'].split('-')[0]]['hosts'].append(instance['name'])
        else:
            all[instance['name'].split('-')[0]] = {'hosts': []}
            all[instance['name'].split('-')[0]]['hosts'].append(instance['name'])

    return all

def get_all_vars():
    vars = {}
    # for etc hsots
    hosts = []
    for instance in responce['instances']:
        hosts.append(instance['networkInterfaces'][0]['primaryV4Address']['address'] + "    " + instance['name'])
    vars['hosts'] = hosts
    return vars


def get_list():
    result_inventory = inventory | get_groups()
    result_inventory['_meta']['hostvars'] = get_hostvars()
    result_inventory['all']['children'] = list(get_groups().keys())
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
    "vars": { 
        'erlang_cookie': 'SRENBEZHALWYXNCYTJNG',
        'rabbitmq_master': 'rabbit-0'
    }
  }
}

token = open("token").read()
folder_id = "b1gaf9l1lrdtb72755nd"



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