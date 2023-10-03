# Ensure the custom HTTP header response in Nginx

# Update package list
exec { 'update':
  command => '/usr/bin/apt-get update',
  path    => '/usr/bin',
  logoutput => true,
}

# Install Nginx if not already installed
package { 'nginx':
  ensure => 'installed',
}

# Define the custom header value
$custom_header = "add_header X-Served-By \$hostname;"

# Add the custom header configuration to Nginx
file_line { 'http_header':
  path  => '/etc/nginx/nginx.conf',
  line  => $custom_header,
  match => '^http {',
}

# Restart Nginx to apply the changes
service { 'nginx':
  ensure  => 'running',
  enable  => true,
  require => [Package['nginx'], File_line['http_header']],
}

