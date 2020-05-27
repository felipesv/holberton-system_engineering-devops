exec { 'fixNginxService':
  command => 'sed -i s/15/2000/ /etc/default/nginx',
  path    => '/bin',
}
service { 'nginx':
  ensure    => running,
  subscribe => Exec['fixNginxService'],
}
