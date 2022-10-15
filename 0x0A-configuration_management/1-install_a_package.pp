# Installs the package: Flask version: 2.1.0 Using The Puppet Configuration Management System

package {'Flask':
  ensure   => '2.1.0',
  provider => pip3,
}
