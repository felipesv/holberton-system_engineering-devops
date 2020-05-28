# change the limit 15 with 4096 in all coincidences
exec { 'change limit':
  command => 'sed -i "s/15/4096/g" nginx',
  cwd     => '/etc/default/',
  path    => '/bin/',
} ->
# restart the nginx service
exec { 'restart-nginx':
  command => 'nginx restart',
  path    => '/etc/init.d/',
}
