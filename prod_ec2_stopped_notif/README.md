
# Production Instance Monitoring System

## Overview
This project is designed to monitor EC2 instances in a production environment to ensure they remain healthy and operational. It aims to minimize downtime and maintain optimal service for customers.

## Components
- **AWS EventBridge**: Monitors EC2 instances, specifically those tagged with 'Prod', indicating they are production instances.
- **AWS Lambda (main.py)**: Triggered by EventBridge notifications. It executes when an instance with the 'Prod' tag is stopped.
- **AWS SNS**: Used for sending notifications. When the Lambda function is triggered, it sends a message to an SNS topic.

## main.py
The Python script (`main.py`) is the core of the Lambda function. It utilizes Boto3 to interact with AWS services. Upon triggering, it sends a notification to the specified SNS topic, alerting about the stopped production instance.

## Objective
The primary objective is to quickly notify the relevant team when a production instance is stopped, enabling prompt response and issue resolution to maintain seamless service.

## Setup and Configuration
Details about setting up EventBridge, Lambda, and SNS should be provided here.

---

> Note: This README assumes that AWS resources like EC2, EventBridge and SNS are already configured.

