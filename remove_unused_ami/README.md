
# UNUSED AMI REMOVER

## Overview
This Python project is designed to manage Amazon Machine Images (AMIs) on AWS EC2. It automates the process of deregistering unused AMIs in the specified AWS region.

## Functionality
- The script uses Boto3 to interact with AWS EC2.
- It first retrieves a list of instances in the 'ap-south-1' region and collects the AMIs used by these instances.
- It then retrieves a list of AMIs owned by the user.
- The script compares these lists and deregisters any AMI that is owned by the user but not currently used by any instance.

## Usage
- Ensure AWS credentials are configured properly.
- Run `main.py` to execute the script.
- Unused AMIs will be automatically deregistered.

## Requirements
- Boto3
- AWS account with configured credentials

## Note
- Use caution when running this script as it will deregister AMIs which might be important.
