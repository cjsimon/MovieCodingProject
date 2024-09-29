resource "digitalocean_firewall" "vpn_firewall" {
  name = "${var.environment}-vpn-firewall"
  droplet_ids = [digitalocean_droplet.host.*.id]
  inbound_rule {
    protocol         = "tcp"
    port_range       = "22"
    source_addresses = var.app_firewall_whitelist_ips
  }
}
