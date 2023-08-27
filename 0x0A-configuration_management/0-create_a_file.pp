# create a file in /tmp/school and write into it

file { '/tmp/school':
  ensure  => present,
  content => 'I love Puppet',
  owner   => 'www-data',
  group   => 'www-data',
  mode    => '0744',
}
