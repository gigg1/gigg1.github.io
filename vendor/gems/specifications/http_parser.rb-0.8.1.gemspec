# frozen_string_literal: true

Gem::Specification.new do |s|
  s.name          = "http_parser.rb"
  s.version       = "0.8.1"
  s.authors       = ["Marc-Andre Cournoyer", "Aman Gupta"]
  s.email         = ["macournoyer@gmail.com", "aman@tmm1.net"]
  s.homepage      = "https://github.com/tmm1/http_parser.rb"
  s.summary       = "Simple callback-based HTTP request/response parser"
  s.description   = "Ruby bindings to the joyent http-parser"
  s.licenses      = ["MIT"]
  s.require_paths = ["lib"]
  s.extensions    = []
  s.files         = []
  s.bindir        = "bin"
  s.executables   = []
  s.required_ruby_version = Gem::Requirement.new(">= 0")
  s.date          = Time.utc(2018, 5, 12)
end
