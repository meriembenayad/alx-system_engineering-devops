#!/usr/bin/env ruby
puts ARGV[0].scan(/\[from:(.*?)\]\s\[to:(.*?)\]\s\[flags:(.*?){1,3}\]/).join(",")
