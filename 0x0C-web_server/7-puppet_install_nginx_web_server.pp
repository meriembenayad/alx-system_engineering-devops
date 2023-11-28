# Configure server with Puppet
class { 'nginx' }

nginx::resource::server { 'default':
    listen_port	=> 80,
    index_files	=> ['index.html'],
    www_root	=> '/var/www/html',
}

file { '/var/www/html/index.html':
    ensure	=> file,
    content	=> 'Hello World!',
}

nginx::resource::location { 'redirect_me':
    location => '/redirect_me',
    server => 'default',
    return => '301 return https://www.youtube.com/watch?v=QH2-TGUlwu4',
    location_alias => '/var/www/html',
}
