# frozen_string_literal: true

# Generates a proper .gemspec stub file for eventmachine from its .gem package,
# so RubyGems can recognize it as an installed gem.

require "rubygems/package"

gem_home = "/Users/giggliu/Downloads/PrivateInformation/Website/gigg1.github.io/vendor/gems"
pkg = "/Users/giggliu/Downloads/PrivateInformation/Website/gigg1.github.io/vendor/gems_cache/eventmachine-1.2.7.gem"
spec = Gem::Package.new(pkg).spec

gemspec_path = File.join(gem_home, "specifications/eventmachine-1.2.7.gemspec")

File.open(gemspec_path, "w") do |f|
  f.puts "# -*- encoding: utf-8 -*-"
  f.puts "# stub: eventmachine 1.2.7 ruby lib"
  f.puts
  f.puts "Gem::Specification.new do |s|"
  f.puts "  s.name = #{spec.name.inspect}"
  f.puts "  s.version = #{spec.version.to_s.inspect}"
  f.puts "  s.authors = #{spec.authors.inspect}"
  f.puts "  s.email = #{spec.email.inspect}"
  f.puts "  s.homepage = #{spec.homepage.inspect}"
  f.puts "  s.summary = #{spec.summary.inspect}"
  f.puts "  s.description = #{spec.description.inspect}"
  f.puts "  s.license = #{spec.license.inspect}"
  f.puts "  s.require_paths = #{spec.require_paths.inspect}"
  f.puts "  s.extensions = #{spec.extensions.inspect}"
  f.puts "  s.files = #{spec.files.inspect}"
  f.puts "  s.extra_rdoc_files = #{spec.extra_rdoc_files.inspect}"
  f.puts "  s.rdoc_options = #{spec.rdoc_options.inspect}"
  f.puts "  s.bindir = #{spec.bindir.inspect}"
  f.puts "  s.executables = #{spec.executables.inspect}"
  req = spec.required_ruby_version ? "Gem::Requirement.new(#{spec.required_ruby_version.to_s.inspect})" : 'Gem::Requirement.new(">= 0")'
  f.puts "  s.required_ruby_version = #{req}"
  f.puts "  s.date = #{spec.date.inspect}"
  spec.runtime_dependencies.each do |d|
    f.puts "  s.add_runtime_dependency #{d.name.inspect}, #{d.requirement.to_s.inspect}"
  end
  spec.development_dependencies.each do |d|
    f.puts "  s.add_development_dependency #{d.name.inspect}, #{d.requirement.to_s.inspect}"
  end
  f.puts "end"
end

puts "gemspec written to #{gemspec_path}"
