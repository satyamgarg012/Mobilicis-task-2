import boto3

def create_cpu_alarm(instance_id):
    cloudwatch = boto3.client('cloudwatch')

    alarm_name = 'HighCPUAlarm'
    metric_name = 'CPUUtilization'
    namespace = 'AWS/EC2'
    comparison_operator = 'GreaterThanOrEqualToThreshold'
    threshold = 80
    evaluation_periods = 5
    period = 60  # in seconds
    alarm_description = 'Alarm when CPU exceeds 80% for 5 consecutive minutes'
    alarm_actions = ['arn:aws:sns:us-east-1:123456789012:MyTopic']  # Replace with your SNS topic ARN

    response = cloudwatch.put_metric_alarm(
        AlarmName=alarm_name,
        AlarmDescription=alarm_description,
        ActionsEnabled=True,
        AlarmActions=alarm_actions,
        MetricName=metric_name,
        Namespace=namespace,
        Statistic='Average',
        Dimensions=[
            {
                'Name': 'InstanceId',
                'Value': instance_id
            },
        ],
        Period=period,
        EvaluationPeriods=evaluation_periods,
        Threshold=threshold,
        ComparisonOperator=comparison_operator
    )

    print("CloudWatch alarm created successfully.")

# Replace 'instance_id' with the actual EC2 instance ID
instance_id = 'i-0123456789abcdef0'
create_cpu_alarm(instance_id)
