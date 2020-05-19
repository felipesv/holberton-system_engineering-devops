# Change the phpp to php using sed command 
# 's/phpp/php/g'
# -i: in place
# s: substitute command
# phpp: word to replace
# php: new text
# g: global, relpace in all matches

exec { 'change phpp to php':
  command => "sed -i 's/phpp/php/g' wp-settings.php",
  cwd => '/var/www/html/',
  path => '/bin/',
}

# restart apache service
service { 'restart-apache2':
  name => 'apache2',
  hasrestart => true,
}
