# Fix our stack; Nginx is responsible for handling failed requests.

exec {'Change nginx limit':
  command => '/bin/sed -i \'s/ULIM.*//\' /etc/default/nginx'
}

exec {'Restart Nginx':
  command => '/usr/sbin/service nginx restart'
}
