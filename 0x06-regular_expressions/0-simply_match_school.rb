#!/usr/bin/env ruby
# Match the word "School" as a whole word

# Check if there is exactly one command-line argument
if ARGV.length != 1
  puts "Usage: ./0-simply_match_school \"School\""
  exit(1)
end

puts ARGV[0].scan(/School/).join
