
# EC2 Instance Scheduler

This Python project contains two scripts designed to manage AWS EC2 instances. The scripts are intended to be used with AWS Lambda functions for automating the starting and stopping of EC2 instances based on specific tags.

## Files

1. `start.py` - This script is used to start EC2 instances. It filters instances with the tag `Type: Scheduled` and initiates their startup.

2. `stop.py` - This script is used to stop EC2 instances. It filters instances with the tag `Type: Scheduled` and initiates their shutdown.

## Usage

These scripts are designed to be deployed as AWS Lambda functions. They can be scheduled to run at specific times to automate the starting and stopping of EC2 instances, which can be useful for managing costs and resources.

### Prerequisites

- AWS account with access to EC2 and Lambda services.
- Necessary IAM roles and permissions for Lambda functions to interact with EC2 instances.

### Deployment

1. Create two Lambda functions in AWS, one for each script.
2. Ensure the Lambda functions have the appropriate IAM roles to access and modify EC2 instances.
3. Set up a trigger, like Amazon CloudWatch Events, to run these functions according to your schedule.

## Note

- Ensure that your EC2 instances are tagged correctly with `Type: Scheduled` to be affected by these scripts.
- Modify the scripts if you need to target instances with different tags or criteria.
