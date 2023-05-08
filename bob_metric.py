import boto3
import gzip
import base64
import json
from datetime import datetime
import pytz

def lambda_handler(event, context):
    print("Lambda function started")  # Added log message

    # Initialize CloudWatch client
    cloudwatch = boto3.client('cloudwatch')

    # Decode and decompress CloudWatch Logs data
    logs_data = gzip.decompress(base64.b64decode(event['awslogs']['data']))
    logs_json = json.loads(logs_data)

    # Process log events
    for log_event in logs_json['logEvents']:
        # Extract log message
        log_message = log_event['message']
        print(f"Processing log message: {log_message}")  # Added log message

        # Generate custom metric for logs containing the specified text
        if 'try to post' in log_message:
            print("Log message contains 'try to post'")  # Added log message

            # Get the current date in the Australia/Sydney timezone
            sydney_tz = pytz.timezone('Australia/Sydney')
            current_date = datetime.now(sydney_tz).strftime('%Y-%m-%d')

            # Create a metric name with the current date
            metric_name = f'BobBotThreadMessageCount-{current_date}'
            print(f"Generated metric name: {metric_name}")  # Added log message

            cloudwatch.put_metric_data(
                Namespace='BobBotLogMetrics',
                MetricData=[
                    {
                        'MetricName': metric_name,
                        'Value': 1,
                        'Unit': 'Count'
                    }
                ]
            )
            print("Successfully put metric data")  # Added log message

    return {
        'statusCode': 200,
        'body': json.dumps('Successfully processed logs and generated custom metrics.')
    }