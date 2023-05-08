# AWS Lambda Log Processor

This project deploys an AWS Lambda function that processes CloudWatch Logs and generates custom metrics based on the occurrences of a specific text in the logs. The Lambda function is triggered by CloudWatch Logs and generates daily custom metrics using the Australia/Sydney timezone.

## Prerequisites

- [Node.js](https://nodejs.org/en/) installed (for the Serverless Framework)
- [Serverless Framework](https://www.serverless.com/) installed
- AWS account with the necessary permissions to create Lambda functions, CloudWatch Logs triggers, and CloudWatch custom metrics

## Project Structure

- `bob_metric.py`: Lambda function code that processes CloudWatch Logs and generates custom metrics
- `requirements.txt`: Python dependencies required for the Lambda function (boto3 and pytz)
- `serverless.yml`: Serverless Framework configuration file for deploying the Lambda function and setting up the CloudWatch Logs trigger



## Testing

1. Create a virtual environment:

   
   python -m venv .venv
   

2. Activate the virtual environment:

   - On macOS and Linux:

     
     source .venv/bin/activate
     

   - On Windows:

     
     .\venv\Scripts\activate
     

3. Install the Python dependencies:

   
   pip install -r requirements.txt
   

4. Run the tests:

   
   pytest test_bob_metric.py

The tests check if the Lambda function processes the logs correctly and generates the custom metric when the specified text is present in the log entry.

## Deployment

1. Install the Serverless Framework globally:

   
   npm install -g serverless
   

2. Configure your AWS credentials:

   
   serverless config credentials --provider aws --key <your_aws_access_key> --secret <your_aws_secret_key>
   

3. Deploy the service:

   
   serverless deploy
   

After deployment, the Lambda function will be triggered by CloudWatch Logs, process the logs, and generate custom metrics based on the filtering logic.



## Customization

To customize the filtering logic or the custom metric generation, modify the `bob_metric.py` file. Update the `serverless.yml` file to change the AWS region, stage, or other service configurations.# bobbot-metrics
