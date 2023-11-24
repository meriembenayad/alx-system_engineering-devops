exec { 'pkill':
  command => 'pkill killmenow',
  path    => ['/bin', '/usr/bin'],
  returns => [0, 1],
}
