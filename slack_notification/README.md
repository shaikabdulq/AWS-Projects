
#  Production Instance Slack Alert

## Overview
This script designed to be deployed to AWS Lambda function that send alerts to a Slack channel through encrypted webhook URL when a production EC2 Instance is stopped.

## Features
- Slack integration using a webhook.
- Secure handling of sensitive data (Slack webhook URL) using AWS KMS for decryption.

## Dependencies
- `requests`: To make HTTP requests to the Slack webhook.
- `json`: To handle JSON data.
- `os`: To access environment variables.
- `boto3`: AWS SDK for Python, used for decrypting the encrypted Slack webhook URL.
- `base64`: To decode base64 encoded data.

## Usage
The script `slack_alert.py` is designed to be deployed as an AWS Lambda function. It can be integrated with AWS EventBridge event which gets triggered when a production EC2 instance is stopped. It sends a predefined message ("EC2 Instance Stopped") to a specified Slack channel when triggered.

### Environment Variables
- `SLACK_WEBHOOK`: The encrypted Slack webhook URL.
- `AWS_LAMBDA_FUNCTION_NAME`: The name of the Lambda function, used in the decryption context.

## Security
The Slack webhook URL is encrypted and stored in an environment variable. It is decrypted at runtime using AWS KMS.

> Note: This README assumes that AWS resources like EC2, EventBridge and KMS are already configured.

