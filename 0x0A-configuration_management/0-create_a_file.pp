# Create a file using the Puppet configuration management system.

file {'/tmp/school': # Specifying a file resource
  ensure  =>  file,
  mode    =>  '0744',
  owner   =>  'www-data',
  group   =>  'www-data',
  content =>  'I love Puppet',
}
