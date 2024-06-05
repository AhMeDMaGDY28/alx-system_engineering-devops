# a fix for ubuntu 14.04

exec { 'Fix miss-spling problem':
  command  => 'sudo sed -i "s/.phpp/.php/" /var/www/html/wp-settings.php',
  provider => shell,
}
