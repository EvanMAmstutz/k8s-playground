variable "base_name" {
  description = "default name for all resources"
  type = string
}

variable "aws_region" {
  description = "region for aws resources"
  type = string
}

variable "azure_sub_id" {
  description = "subscription id for azure environment"
  type = string
}

variable "gcp_region" {
  description = "region for gcp resources"
  type = string
}
