#Install Flask from pip3 using Puppet
package { 'Flask':
  ensure   => '2.1.0',
  provider => 'pip3',
}
