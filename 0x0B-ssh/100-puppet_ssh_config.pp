# Set up config for ssh client
include stdlib

file_line { 'Configure no password':
  ensure => present,
  path   => '/etc/ssh/ssh_config',
  lines => [
    '  IdentityFile ~/.ssh/school',
    '  PasswordAuthentication no',
  ],
  replace => true,
}