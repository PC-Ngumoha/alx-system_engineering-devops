# Kills a running process.
exec {'pkill':
  command => '/usr/bin/pkill -15 killmenow',
}
