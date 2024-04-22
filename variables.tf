 variable "namespace" {
   type        = string
   description = "String used for prefix resources."
 }

 variable "location" {
   type        = string
   description = "Azure Resource Group location"
 }

 variable "domain_name" {
   type        = string
   description = "Domain for accessing the Weights & Biases UI."
 }

 variable "subdomain" {
   type        = string
   default     = null
   description = "Subdomain for accessing the Weights & Biases UI. Default creates record at Route53 Route."
 }

 variable "license" {
   type        = string
   description = "Your wandb/local license"
 }