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
