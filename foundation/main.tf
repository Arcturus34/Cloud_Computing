terraform {
  required_providers {
    scaleway = {
      source = "scaleway/scaleway"
    }
  }
  required_version = ">= 0.13"
}

provider "scaleway" {
  zone   = "fr-par-1"
  region = "fr-par"
}

#Registre de Conteneur
resource "scaleway_registry_namespace" "main" {
  name        = "main-cr"
  description = "Main container registry"
  is_public   = false
}

resource "scaleway_vpc_private_network" "pn" {}

#Cluster Kubernetes
resource "scaleway_k8s_cluster" "cluster" {
  name                        = "tf-cluster"
  version                     = "1.29.1"
  cni                         = "cilium"
  private_network_id          = scaleway_vpc_private_network.pn.id
  delete_additional_resources = false
}

resource "scaleway_rdb_instance" "main" {
  name           = "test-rdb"
  node_type      = "DB-DEV-S"
  engine         = "PostgreSQL-15"
  is_ha_cluster  = true
  disable_backup = true
  user_name      = "Soulairol"
  password       = "esirem"
}

#Base de donnees development
resource "scaleway_rdb_database" "development" {
  instance_id = scaleway_rdb_instance.main.id
  name        = "development-database"
}

#Base de donnees production
resource "scaleway_rdb_database" "production" {
  instance_id = scaleway_rdb_instance.main.id
  name        = "production-database"
}

#DNS
resource "scaleway_domain_record" "www1" {
  dns_zone = "calculatrice-Soulairol-polytech-dijon.kiowy.net"
  name     = "www1"
  type     = "A"
  data     = "1.2.3.4"
  ttl      = 3600
}


resource "scaleway_domain_record" "www2" {
  dns_zone = "calculatrice-dev-Soulairol>-polytech-dijon.kiowy.net"
  name     = "www2"
  type     = "A"
  data     = "1.2.3.4"
  ttl      = 3600
}

resource "scaleway_lb_ip" "main" {
  zone = "fr-par-1"
}

#LoadBalancer
resource "scaleway_lb" "development" {
  ip_ids = [scaleway_lb_ip.main.id]
  zone   = scaleway_lb_ip.main.zone
  type   = "LB-S"
}

resource "scaleway_lb" "production" {
  ip_ids = [scaleway_lb_ip.main.id]
  zone   = scaleway_lb_ip.main.zone
  type   = "LB-S"
}
