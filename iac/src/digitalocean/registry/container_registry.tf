resource "digitalocean_container_registry" "container_registry" {
  name                   = "${var.environment}-registry"
  subscription_tier_slug = "starter"
}
