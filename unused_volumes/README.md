
# Unused Volume Notifier

## Overview
This Python project is designed to help with monitoring and notifying about unused AWS EC2 volumes. It uses AWS SDK for Python (Boto3) to interact with AWS services.

## Functionality
- The script retrieves a list of all volumes in AWS EC2.
- It identifies volumes that are currently unused.
- An email notification is sent about these unused volumes using AWS SNS (Simple Notification Service).

## Prerequisites
- AWS account with access to EC2 and SNS services.
- Boto3 installed and configured with necessary AWS credentials.

## Usage
Run `main.py` to execute the script. It will:
- Fetch all the volumes from AWS EC2.
- Determine the unused volumes.
- Send an email notification with the details of these unused volumes.

## Note
- The script contains a hardcoded SNS topic ARN, which should be modified according to your AWS setup.
