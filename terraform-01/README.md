1. Create file `token` and put in token for connect yandex cloud
2. `terraform apply`
3. Set external ip of created instance in ansible/host.ini
4. `ansible-playbook -i ansible/hosts.ini -vD ansible/install-nginx.yaml`
5. Check `curl http://<external ip>`