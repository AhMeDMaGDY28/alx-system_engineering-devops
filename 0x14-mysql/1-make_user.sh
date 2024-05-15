#!/usr/bin/env bash

sudo ufw allow 3306
# to start mysql
sudo mysql -u root -p2849

# to create user
CREATE USER 'holberton_user'@'localhost' IDENTIFIED WITH mysql_native_password BY 'projectcorrection280hbtn';

# to grant privilages
GRANT ALL PRIVILEGES ON *.* TO 'holberton_user'@'localhost' WITH GRANT OPTION;

# to see the users in mysql
SELECT user,host FROM mysql.user;

# to see privilages
SHOW GRANTS FOR holberton_user;
