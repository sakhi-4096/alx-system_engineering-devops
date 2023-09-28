# Install Nginx package
package { 'nginx':
  ensure => 'installed',
}

# Create the index.html file
file { '/var/www/html/index.html':
  ensure  => 'file',
  content => 'Hello World!',
}

# Configure Nginx
file { '/etc/nginx/sites-available/default':
  ensure  => 'file',
  content => "
    server {
        listen 80 default_server;
        server_name _;

        location /redirect_me {
            return 301 https://youtube.com/;
        }
    }
  ",
  notify  => Service['nginx'],
}

# Enable and start Nginx service
service { 'nginx':
  ensure => 'running',
  enable => true,
}

# Restart Nginx when the configuration file changes
file { '/etc/nginx/sites-available/default':
  require => Service['nginx'],
  notify  => Service['nginx'],
}