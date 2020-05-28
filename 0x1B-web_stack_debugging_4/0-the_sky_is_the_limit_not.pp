exec { 'change limit':
  command => 'sed -i "s/15/4096/" /etc/default/nginx',
  path    => '/bin/sed'
}
exec { 'restar nginx':
  command => 'service restar nginx',
  path    => '/usr/sbin/service'
}
