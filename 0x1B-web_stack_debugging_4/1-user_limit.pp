# Puppet manifest to fix file limit for the 'hbton' user.

# Fix hard file limit for hbton user
exec { 'increase-hard-file-limit-for-hbton-user':
  command => 'sed -i "/holberton hard/s/5/50000/" /etc/security/limits.conf',
  path    => '/usr/local/bin/:/bin/'
}

# Increase soft file limit for hbton user
exec { 'increase-soft-file-limit-for-hbton-user':
  command => 'sed -i "/holberton soft/s/4/50000/" /etc/security/limits.conf',
  path    => '/usr/local/bin/:/bin/'
}