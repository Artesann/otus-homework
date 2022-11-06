1. `terraform apply`
2. Set external ip of created instance in ansible/host.ini
3. `ansible-playbook -i ansible/hosts.ini -vD ansible/install-nginx.yaml`
4. To check `curl http://<external ip>`