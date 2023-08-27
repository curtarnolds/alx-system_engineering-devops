# execute a command

exec { 'kill killmenow':
  command => '/usr/bin/pkill killmenow'
}
