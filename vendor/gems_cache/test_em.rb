# frozen_string_literal: true

require "rubygems"

gem_home = "/Users/giggliu/Downloads/PrivateInformation/Website/gigg1.github.io/vendor/gems"
Gem.use_paths(gem_home)

path = File.join(gem_home, "specifications/eventmachine-1.2.7.gemspec")
s = Gem::Specification.load(path)
if s.nil?
  puts "loaded: nil"
else
  puts "loaded: #{s.full_name}"
  puts "version class: #{s.version.class}"
  begin
    s.validate
    puts "validate: ok"
  rescue => e
    puts "validate raised: #{e.message}"
  end
end

# Now check activation behavior
require "rubygems/dependency_installer"
puts "--- try activate eventmachine ---"
begin
  gem "eventmachine"
  puts "gem 'eventmachine' OK, loaded from #{$LOADED_FEATURES.grep(/eventmachine/).last}"
rescue => e
  puts "gem 'eventmachine' FAILED: #{e.class}: #{e.message}"
end
