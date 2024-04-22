# Weights & Biases Lab

## Overview

The goal for this lab was to deploy Weights & Biases Server either in a public cloud or local infrastructure. Once the server is deployed, then complete at least 10 runs utilizing the W&B Python SDK.

For this lab I chose to deploy the Weights and Biases Server on Azure infrastructure by following the doucmented process for [deploying on the Azure platform](https://docs.wandb.ai/guides/hosting/self-managed/azure-tf). My reasoning for doing this was two fold:

1. I wanted to increase my knowledge, understanding, and utilization of the Microsoft Azure cloud platform. I figured this was the perfect opportunity for that.

2. This approach utilizes the Infrastructure as Code application Terraform for automation and makes use of the [W&B Server Azure Terraform Module](https://registry.terraform.io/modules/wandb/wandb/azurerm/latest) to further simplify the deployment process.

To complete the 10 runs once the Weights & Biases Server was established I followed the [Quickstart guide](https://docs.wandb.ai/quickstart) to create a script for completing runs on the server. This did start out as a really basic and simple script that achieved the objective of completing the 10 required runs. While it isn't terribly complex at this time, I did read through the documentation further and figured out how to automate the authentication process using the API key and randomly placed 1-4 runs into groups within a couple projects.

## Terraform Configuration

### Pre-requisites

- Terraform version >= 1.5
- AzureRM provider ~> 3.100
- Azure authentication via Azure CLI or Service Principal

### Summary

The Terraform configuration for this deployment of Weights & Biases is fairly simple. It consists of the `main.tf`, `variables.tf`, `versions.tf`, and `terraform.tfvars` files.

1. `main.tf` - This is where the primary source of the Terraform configuration can be found. Here we will configure the AzureRm, Kubernetes, and Helm providers. Additionaly this is whre the [W&B Server Azure Terraform Module](https://registry.terraform.io/modules/wandb/wandb/azurerm/latest) is configured and called. This file also has outputs of the server address and URL once deployment has completed.

2. `variables.tf`- This configuration file is where we establish our variables. For this configuration we have the following **required variables**:

    | Variable | Description |
    | :-------- | :----------- |
    | namespace | String used for prefix resources. |
    | location | Azure Resource Group location. |
    | domain_name | Domain for accessing the Weights & Biases UI.|
    | sub_domain | Subdomain for accessing the Weights & Biases UI. |
    | license | Your wandb/local license |

3. `versions.tf` - This configuration file establishes the required versions of Terraform and the AzureRM  provider.

4. `terraform.tfvars` - A file used as part of normal Terraform operations to set the values for the required varables.

## Python Script

The python script used to generate and complete runs is `runners.py`. This started out as a script that would login to the W&B Server, prompt for the API key, then generate and complete a run.

I then improved the script to automatically authenticate to the W&B Server and complete 10 runs. After further reading into the documentation I decided to further improve the script to additionally group between 1-4 runs into groups until it had completed at least 20 runs.

# Project Images

This section will contain the required images for this lab, consisting of **at least** the following images

1. W&B Server Homepage
2. System Admin page
3. Project with at least 10 runs completed
4. Screenshot of infrastructure resources from the Azure Resource Groups.

## W&B Server Homepage

![Image of the W&B Server Homepage](images/home.png)

## Projects Page

![Image of the W&B Server Projects page](images/projects.png)

## System Admin Page

![Image of the W&B Server System Admin Page](images/sysadmin.png)

## Project With At Least 10 Completed Runs

![Image of project with at least 10 completed runs](images/all-runs.png)

## Infrastructure Resources

![Image of Resources in wandb1-rg](images/wandb1-rg.png)
![Image of MC_wandb1_wandb1-cluster_eastus-rg](images/mc_wandb1_wandb1-cluster_eastus-rg.png)

# Additional Images

Additional images of runs that were completed and grouped together via the script improvements.

![Image of project with completed runs grouped together](images/group-lab.png)
![Image of project with completed runs grouped together](images/group-lab2.png)