#!/usr/bin/env ruby
SENDER = ARGV[0].scan(/from:([\w\d+]+)/).join
RECEIVER = ARGV[0].scan(/to:([+\d]+)/).join
FLAGS = ARGV[0].scan(/flags:([\d:-]+)/).join
puts "#{SENDER},#{RECEIVER},#{FLAGS}"
