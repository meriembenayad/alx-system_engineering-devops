# Install nginx
package { 'nginx':
  ensure => 'installed',
}

# file index
file { '/var/www/html/index.html':
  ensure  => 'file',
  content => 'Hello World!',
  mode    => '0644',
  require => Package['nginx'],
}

# redirect_me file
file_line { 'redirect_me':
  ensure => present,
  path   => '/etc/nginx/sites-available/default',
  after  => 'server_name _;'
  line   => '
    location /redirect_me {
      return 301 https://www.youtube.com/watch?v=QH2-TGUlwu4;
    }',
}

# Stop nginx
exec { 'stop service':
  command => 'sudo service nginx stop',
  path    => ['/bin', '/usr/bin', '/usr/sbin'],
}

# Run nginx
exec { 'start service':
  command => 'sudo service nginx start',
  path    => ['/bin', '/usr/bin', '/usr/sbin'],
}
