# A puppet manuscript to replace a line in a file
$file_to_edit = '/var/www/html/wp-settings.php'
exec { 'replace_line':
  command => "sed -i 's/phpp/php/g' ${file_to_edit}",
  path    => ['/bin','/usr/bin']
}
