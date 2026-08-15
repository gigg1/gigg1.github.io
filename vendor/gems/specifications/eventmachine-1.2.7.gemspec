# frozen_string_literal: true

# Minimal stub gemspec for a manually-installed eventmachine.
# RubyGems requires the gemspec to validate; files listed must exist.

Gem::Specification.new do |s|
  s.name          = "eventmachine"
  s.version       = "1.2.7"
  s.authors       = ["Francis Cianfrocca", "Aman Gupta"]
  s.email         = ["garbagecat10@gmail.com", "aman@tmm1.net"]
  s.homepage      = "http://rubyeventmachine.com"
  s.summary       = "Ruby/EventMachine library"
  s.description   = "EventMachine implements a fast, single-threaded engine for arbitrary network communications."
  s.license       = "Ruby"
  s.require_paths = ["lib"]
  s.extensions    = []
  s.files         = ["lib/eventmachine.rb", "lib/jeventmachine.rb", "lib/rubyeventmachine.bundle"]
  s.bindir        = "bin"
  s.executables   = []
  s.required_ruby_version = Gem::Requirement.new(">= 0")
  s.date          = Time.utc(2018, 5, 12)
  s.add_development_dependency "test-unit", "~> 2.0"
  s.add_development_dependency "rake-compiler", "~> 0.9.5"
  s.add_development_dependency "rake-compiler-dock", "~> 0.5.1"
end
