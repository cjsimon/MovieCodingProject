variable "environment" {
  description = "The environment to deploy"
  type        = string
  
  validation {
    condition     = contains(["testing", "development", "staging", "production"], var.environment)
    error_message = "Invalid environment. Valid environments: \"testing\", \"development\", \"staging\", or \"production\""
  }
}

variable "do_token" {
  description = "The DigitalOcean API token"
  type        = string
}

variable "app_firewall_whitelist_ips" {
  description = "The list of IPs allowed through the app firewall"
  type        = list(string)
}
