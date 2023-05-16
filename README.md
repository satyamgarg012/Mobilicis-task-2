# Mobilicis-task-2

## The code is in Master Branch 

Certainly! Here's a Python script that uses the Boto3 library to create a CloudWatch alarm that triggers an alert when the CPU usage of an EC2 instance exceeds 80% for five consecutive minutes.

Make sure to replace 'instance_id' with the actual ID of your EC2 instance. Additionally, replace 'arn:aws:sns:us-east-1:123456789012:MyTopic' with the ARN of your SNS topic that should receive the alert notifications.
