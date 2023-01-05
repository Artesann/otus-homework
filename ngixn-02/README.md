## Set up any webserver, database and fault-tolerant nginx loadbalancer

I've tried it in yandex cloud, but VRRP does not work because of arp poroxy. So I did it with vagrant.

To start vagrant: 

1. Add public key for ssh in `user_setup.sh`
2. `vagrant up`

In ansible folder: 

1. In ansible dirrectory `ansible-galaxy instll -r requirements.yaml`  
2. Make sure ips in hosts.ini are correct in host.ini and `ansible-playbook -i hosts.ini -vD start.yaml`
3. Virtual address is `192.168.0.50`. To check webapp run `curl http://192.168.0.50`. To connect to database `mysql -u root -p -h 192.168.0.50`, password is `password`