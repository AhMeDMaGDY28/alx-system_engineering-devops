# Change the OS configuration so that it is possible to login with

exec { 'change-os-configuration-for-holberton-user':
  command => '/bin/echo -e "holberton soft nofile 4096\nholberton hard nofile 8192" >> /etc/security/limits.conf',
  unless  => '/bin/grep -q "holberton soft nofile 4096" /etc/security/limits.conf',
}
