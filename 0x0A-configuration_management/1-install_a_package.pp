# Install Flask 2.1.0 and update Werkzeug
package { 'werkzeug':
  ensure   => '0.16.1',
  provider => 'pip3',
}

package { 'flask':
  ensure   => '2.1.0',
  provider => 'pip3',
}