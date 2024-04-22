provider "azurerm" {
  features {}
}

provider "kubernetes" {
  host                   = module.wandb.cluster_host
  cluster_ca_certificate = base64decode(module.wandb.cluster_ca_certificate)
  client_key             = base64decode(module.wandb.cluster_client_key)
  client_certificate     = base64decode(module.wandb.cluster_client_certificate)
}

provider "helm" {
  kubernetes {
    host                   = module.wandb.cluster_host
    cluster_ca_certificate = base64decode(module.wandb.cluster_ca_certificate)
    client_key             = base64decode(module.wandb.cluster_client_key)
    client_certificate     = base64decode(module.wandb.cluster_client_certificate)
  }
}

# Spin up all required services
module "wandb" {
  source  = "wandb/wandb/azurerm"
  version = "~> 1.2"

  namespace   = var.namespace
  location    = var.location
  license     = var.license
  domain_name = var.domain_name
  subdomain   = var.subdomain

  deletion_protection = false

  tags = {
    "Example" : "PublicDns"
  }
}

output "address" {
  value = module.wandb.address
}

output "url" {
  value = module.wandb.url
}