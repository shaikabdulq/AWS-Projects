
# Python Project - Slack Alert

## Overview
This project contains a Python script designed to send alerts to a Slack channel. 

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
The script `slack_alert.py` is designed to be deployed as an AWS Lambda function. It sends a predefined message ("EC2 Instance Stopped") to a specified Slack channel when triggered.

### Environment Variables
- `SLACK_WEBHOOK`: The encrypted Slack webhook URL.
- `AWS_LAMBDA_FUNCTION_NAME`: The name of the Lambda function, used in the decryption context.

## Security
The Slack webhook URL is encrypted and stored in an environment variable. It is decrypted at runtime using AWS KMS.

