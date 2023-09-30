# Script to install nginx using puppet

package { 'nginx':
  ensure => 'present',
}

exec { 'install':
  command  => 'sudo apt-get update ; sudo apt-get -y install nginx',
  provider => shell,
}

exec { 'Hello':
  command  => 'echo "Hello World!" | sudo tee /var/www/html/index.html',
  provider => shell,
}

exec { 'configure_redirect':
  command  => 'sudo sed -i "s/listen 80 default_server;/listen 80 default_server;\\n\\tlocation \/redirect_me {\\n\\t\\treturn 301 https:\/\/google.com\/;\\n\\t}/" /etc/nginx/sites-available/default',
  provider => shell,
  require  => Exec['install'], # Ensure that 'install' is executed before configuring redirect
}

exec { 'run':
  command  => 'sudo service nginx restart',
  provider => shell,
  require  => Exec['configure_redirect'], # Ensure that 'configure_redirect' is executed before restarting Nginx
}
