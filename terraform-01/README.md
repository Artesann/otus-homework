## Hello Terraform
### Task is simply run nginx in yandex cloud via terrafrom ans ansible

In terraform folder:

1. `terraform init`
2. `terrafrom apply`

In ansible folder:

1. `ansible-playbook -i inventory.py -vD start-nginx.yaml`
2. Check `curl http://<external ip>`