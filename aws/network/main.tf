terraform {
}

provider "aws" {
  region = var.aws_region
}

module "aws_setup" {
  source = "./modules/aws-onboarding"
  base_name = var.base_name
}
