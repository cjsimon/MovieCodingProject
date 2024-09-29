resource "digitalocean_droplet" "host" {
  count  = 1
  name   = "${var.environment}-host"
  region = "nyc3"
  size   = "s-1vcpu-1gb"
  image  = "docker-20-04"
}
