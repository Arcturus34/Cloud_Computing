
![test drawio](https://github.com/user-attachments/assets/3011dbf1-9a22-4cf3-a39a-3e051cee745b)








Terraform used the selected providers to generate the following execution plan. Resource actions are indicated with the following symbols:
  + create

Terraform will perform the following actions:

  # scaleway_domain_record.www1 will be created
  + resource "scaleway_domain_record" "www1" {
      + data            = "1.2.3.4"
      + dns_zone        = "calculatrice-Soulairol-polytech-dijon.kiowy.net"
      + fqdn            = (known after apply)
      + id              = (known after apply)
      + keep_empty_zone = false
      + name            = "www1"
      + priority        = (known after apply)
      + project_id      = (known after apply)
      + root_zone       = (known after apply)
      + ttl             = 3600
      + type            = "A"
    }

  # scaleway_domain_record.www2 will be created
  + resource "scaleway_domain_record" "www2" {
      + data            = "1.2.3.4"
      + dns_zone        = "calculatrice-dev-Soulairol>-polytech-dijon.kiowy.net"
      + fqdn            = (known after apply)
      + id              = (known after apply)
      + keep_empty_zone = false
      + name            = "www2"
      + priority        = (known after apply)
      + project_id      = (known after apply)
      + root_zone       = (known after apply)
      + ttl             = 3600
      + type            = "A"
    }

  # scaleway_k8s_cluster.cluster will be created
  + resource "scaleway_k8s_cluster" "cluster" {
      + apiserver_url               = (known after apply)
      + cni                         = "cilium"
      + created_at                  = (known after apply)
      + delete_additional_resources = false
      + id                          = (known after apply)
      + kubeconfig                  = (sensitive value)
      + name                        = "tf-cluster"
      + organization_id             = (known after apply)
      + private_network_id          = (known after apply)
      + project_id                  = (known after apply)
      + region                      = (known after apply)
      + status                      = (known after apply)
      + type                        = (known after apply)
      + updated_at                  = (known after apply)
      + upgrade_available           = (known after apply)
      + version                     = "1.29.1"
      + wildcard_dns                = (known after apply)
    }

  # scaleway_lb.development will be created
  + resource "scaleway_lb" "development" {
      + id                      = (known after apply)
      + ip_address              = (known after apply)
      + ip_id                   = (known after apply)
      + ip_ids                  = [
          + (known after apply),
        ]
      + ipv6_address            = (known after apply)
      + name                    = (known after apply)
      + organization_id         = (known after apply)
      + project_id              = (known after apply)
      + region                  = (known after apply)
      + ssl_compatibility_level = "ssl_compatibility_level_intermediate"
      + type                    = "LB-S"
      + zone                    = "fr-par-1"
    }

  # scaleway_lb.production will be created
  + resource "scaleway_lb" "production" {
      + id                      = (known after apply)
      + ip_address              = (known after apply)
      + ip_id                   = (known after apply)
      + ip_ids                  = [
          + (known after apply),
        ]
      + ipv6_address            = (known after apply)
      + name                    = (known after apply)
      + organization_id         = (known after apply)
      + project_id              = (known after apply)
      + region                  = (known after apply)
      + ssl_compatibility_level = "ssl_compatibility_level_intermediate"
      + type                    = "LB-S"
      + zone                    = "fr-par-1"
    }

  # scaleway_lb_ip.main will be created
  + resource "scaleway_lb_ip" "main" {
      + id              = (known after apply)
      + ip_address      = (known after apply)
      + is_ipv6         = false
      + lb_id           = (known after apply)
      + organization_id = (known after apply)
      + project_id      = (known after apply)
      + region          = (known after apply)
      + reverse         = (known after apply)
      + zone            = "fr-par-1"
    }

  # scaleway_rdb_database.development will be created
  + resource "scaleway_rdb_database" "development" {
      + id          = (known after apply)
      + instance_id = (known after apply)
      + managed     = (known after apply)
      + name        = "development-database"
      + owner       = (known after apply)
      + region      = (known after apply)
      + size        = (known after apply)
    }

  # scaleway_rdb_database.production will be created
  + resource "scaleway_rdb_database" "production" {
      + id          = (known after apply)
      + instance_id = (known after apply)
      + managed     = (known after apply)
      + name        = "production-database"
      + owner       = (known after apply)
      + region      = (known after apply)
      + size        = (known after apply)
    }

  # scaleway_rdb_instance.main will be created
  + resource "scaleway_rdb_instance" "main" {
      + backup_same_region        = (known after apply)
      + backup_schedule_frequency = (known after apply)
      + backup_schedule_retention = (known after apply)
      + certificate               = (known after apply)
      + disable_backup            = true
      + endpoint_ip               = (known after apply)
      + endpoint_port             = (known after apply)
      + engine                    = "PostgreSQL-15"
      + id                        = (known after apply)
      + is_ha_cluster             = true
      + name                      = "test-rdb"
      + node_type                 = "DB-DEV-S"
      + organization_id           = (known after apply)
      + password                  = (sensitive value)
      + project_id                = (known after apply)
      + read_replicas             = (known after apply)
      + region                    = (known after apply)
      + settings                  = (known after apply)
      + user_name                 = "Soulairol"
      + volume_size_in_gb         = (known after apply)
      + volume_type               = "lssd"
    }

  # scaleway_registry_namespace.main will be created
  + resource "scaleway_registry_namespace" "main" {
      + description     = "Main container registry"
      + endpoint        = (known after apply)
      + id              = (known after apply)
      + is_public       = false
      + name            = "main-cr"
      + organization_id = (known after apply)
      + project_id      = (known after apply)
      + region          = (known after apply)
    }

  # scaleway_vpc_private_network.pn will be created
  + resource "scaleway_vpc_private_network" "pn" {
      + created_at      = (known after apply)
      + id              = (known after apply)
      + is_regional     = (known after apply)
      + name            = (known after apply)
      + organization_id = (known after apply)
      + project_id      = (known after apply)
      + region          = (known after apply)
      + updated_at      = (known after apply)
      + vpc_id          = (known after apply)
      + zone            = (known after apply)
    }

Plan: 11 to add, 0 to change, 0 to destroy.

