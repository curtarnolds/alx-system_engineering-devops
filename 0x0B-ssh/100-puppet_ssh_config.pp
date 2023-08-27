# Set up config for ssh client

ssh_config { 'no_password':
  ensure  => present,
  options => {
    'IdentityFile'           => '~/.ssh/school',
    'PasswordAuthentication' => 'no',
  },
}