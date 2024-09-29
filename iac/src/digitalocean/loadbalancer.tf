resource "digitalocean_loadbalancer" "loadbalancer" {
  name   = "${var.environment}-loadbalancer"
  region = "nyc3"
  forwarding_rule {
    entry_protocol  = "https"
    entry_port      = 443
    target_protocol = "https"
    target_port     = 443
  }
  droplet_ids = [digitalocean_droplet.host.*.id]
}
