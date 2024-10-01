terraform {
  required_providers {
    digitalocean = {
      source = "digitalocean/digitalocean"
      version = "2.42.0"
    }
  }
}

########################
# MovieManager Project #
########################
  
  ############################
  # Shared Project Variables #
  ############################
    
    variable "environment" { type = string }
    variable "app_firewall_whitelist_ips" { type = list(string) }
  
  ######################
  # Provider Variables #
  ######################
    
    ################
    # DigitalOcean #
    ################
      
      variable "do_token" { type = string }
  
  ###################
  # Project Modules #
  ###################
    
    #############
    # Providers #
    #############
      
      # DigitalOcean
      module "moviemanager-digitalocean" {
        source = "./digitalocean"
        
        environment                = "${var.environment}"
        do_token                   = "${var.do_token}"
        app_firewall_whitelist_ips = var.app_firewall_whitelist_ips
      }
