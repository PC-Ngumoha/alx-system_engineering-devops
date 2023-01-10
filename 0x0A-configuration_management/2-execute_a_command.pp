# Executing a command using puppet
exec {'kill script':
  command => '/usr/bin/pkill killmenow',
}
