terraform {
}

provider "azurerm" {
  features {}
}

provider "aws" {
  region = var.aws_region
}

provider "google" {
  project = var.base_name
  region  = var.gcp_region
}

module "azure_setup" {
  source = "./modules/azure-onboarding"
  base_name = var.base_name
}

module "aws_setup" {
  source = "./modules/aws-onboarding"
  base_name = var.base_name
}

module "gcp_setup" {
  source = "./modules/gcp-onboarding"
  project_id = var.base_name
  region = var.gcp_region
}