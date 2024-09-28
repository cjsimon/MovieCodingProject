variable "environment" {
  description = "The environment to deploy (testing, development, staging, production)"
}

provider "digitalocean" {
  token = var.do_token
}

resource "digitalocean_container_registry" "registry" {
  name = "${var.environment}-registry"
}

resource "digitalocean_droplet" "host" {
  count  = 1
  name   = "${var.environment}-host"
  region = "nyc3"
  size   = "s-1vcpu-1gb"
  image  = "docker-20-04"
}

resource "digitalocean_kubernetes_cluster" "cluster" {
  name    = "${var.environment}-cluster"
  region  = "nyc3"
  version = "1.21.5-do.0"
  node_pool {
    name       = "default"
    size       = "s-1vcpu-2gb"
    node_count = 3
  }
}

resource "digitalocean_loadbalancer" "lb" {
  name   = "${var.environment}-lb"
  region = "nyc3"
  forwarding_rule {
    entry_protocol  = "http"
    entry_port      = 80
    target_protocol = "http"
    target_port     = 80
  }
  droplet_ids = [digitalocean_droplet.host.*.id]
}

resource "digitalocean_firewall" "vpn_firewall" {
  name = "${var.environment}-vpn-firewall"
  droplet_ids = [digitalocean_droplet.host.*.id]
  inbound_rule {
    protocol = "tcp"
    port_range = "22"
    source_addresses = var.vpn_ips
  }
}
