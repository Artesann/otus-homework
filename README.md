# This is homework repo for Otus linux-highload course.
Cource link: https://otus.ru/lessons/linux-hl/?int_source=courses_catalog&int_term=operations

Most of tasks done in yandex cloud and some with vagrant and virtual-box.
Purpose of every homework is provise part of infrastracture like fault-tolerant nginx loadbalancer or kafka cluster.

Every homework folder contain `ansible` and `terraform` (or `Vagrantfile`) subfolder. Use terraform to provision infrastracture and ansible to roll up services.

## Terraform
To run terraform you need to initialize some vars.
You can initiaze them in var.tf file (be aware to commit this values) or via env variables.

1. `TF_VAR_token`: access token, can be created by command `yc iam create-token`
2. `TF_VAR_cloud_id`
3. `TF_VAR_folder_id`

Then you can simply ran `terraform init; terraform apply`

## Ansible

Certain instruction how to run ansible is in homework folders. In general terms I use dynamic python inventory to get instances names, groups and ips from yandex cloud. It stores in `infra/ansible/inventory.py`, and all other `inventory.py` is simbolic links. To it works, all instances should be named properly: `{ansible_group_name}-{number}`. For example `kafka-0`, `kafka-1`, `nginx-0` etc. Also you must define env vars to access yandex cloud: `YC_TOKEN` and `YC_FOLDER`. 



