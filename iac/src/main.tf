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
  
  ###################
  # Input Variables #
  ###################
  
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
    
    ####################
    # Provider Modules #
    ####################
      
      # DigitalOcean
      module "moviemanager-digitalocean" {
        source = "./digitalocean"
        
        environment                = "${var.environment}"
        do_token                   = "${var.do_token}"
        app_firewall_whitelist_ips = var.app_firewall_whitelist_ips
      }
      
      #######
      # App #
      #######
        
        module "moviemanager-app" {
          source = "./app"
        }
      
      #######
      # Api #
      #######
        
        module "moviemanager-api" {
          source = "./api"
        }
      
      ############
      # Database #
      ############
        
        module "moviemanager-database" {
          source = "./database"
        }
      
      ######################
      # Container Registry #
      ######################
      
        module "moviemanager-container-registry" {
          source = "./container-registry"
        }
