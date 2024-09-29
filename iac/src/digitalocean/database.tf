resource "digitalocean_droplet" "database" {
  name       = "database-host"
  region     = "nyc3"
  size       = "s-1vcpu-1gb"
  image      = "docker-20-04"
  volume_ids = [digitalocean_volume.dbdata.id]
}

resource "digitalocean_volume" "dbdata" {
  name   = "dbdata"
  region = "nyc3"
  size   = 100
}
