1. Add public key for ssh in vagrantfile
2. `vagrant up`
3. In ansible dirrectory `ansible-galaxy instll -r requirements.yaml`  
4. Make sure ips in hosts.ini are correct in host.ini and `ansible-playbook -i hosts.ini -vD start.yaml`
5. Virtual address in this 192.168.0.50 to check webapp exec `curl http://192.168.0.50`. To connect to database `mysql -u root -p -h 192.168.0.50`, password is `password`