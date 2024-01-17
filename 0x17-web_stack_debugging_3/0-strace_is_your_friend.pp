# Using strace, find out why Apache is returning a 500 error.
# And fix it and then automate it using Puppet

exec { 'fix-wordpress':
  command  => 'sudo sed -i "s/.phpp/.php/" /var/www/html/wp-settings.php',
  provider => shell,
}
