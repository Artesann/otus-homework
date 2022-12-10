import requests
import json
import subprocess
from pprint import pprint

token = ""
folder_id = ""
host_groups = ["iscsi", "initiator"] # instance must contain in name one of it


r = requests.get("https://compute.api.cloud.yandex.net/compute/v1/instances?folderId=" + folder_id, 
    headers={"Authorization": "Bearer " + token})

responce = json.loads(r.text)

inventory = {}
for group in host_groups:
    hosts = []
    for instance in responce['instances']:
        if group in instance['name']:
            hosts.append(instance['networkInterfaces'][0]['primaryV4Address']['oneToOneNat']['address'])
    inventory[group]= {"hosts": hosts}


pprint(inventory, indent=4)


def get_iqn(ip):
    iqn = subprocess.check_output(["ssh", ip, "sudo", "cat", "/etc/iscsi/initiatorname.iscsi"])
    return str(iqn).split('\\n')[-2].split('=')[1]