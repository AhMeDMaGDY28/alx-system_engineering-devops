#!/usr/bin/env bash


# the ip from server2 to make extention for server2
sudo ufw allow from 100.24.238.203 to any port 3306

sudo vim /etc/mysql/mysql.conf.d/mysqld.cnf

