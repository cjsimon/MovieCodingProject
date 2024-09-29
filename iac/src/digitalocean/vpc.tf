resource "digitalocean_vpc" "vpc" {
  name   = "${var.environment}-vpc"
  region = "nyc3"
}
