#!/usr/bin/env ruby
resulting = ARGV[0].scan(/(?:from:)(\d{3}?.\w+)|(?:to:)(\d{3}?.\w+)|(?:flags:)(.{1,2}:.{1,2}:.{1,2}:.{1,2}:.{1,2}[^\]])/).join(',')
output = resulting.split(',', -1)
puts "#{output.at(0)},#{output.at(4)},#{output.at(8)}"
