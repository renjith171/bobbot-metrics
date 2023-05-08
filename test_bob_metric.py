import json
import base64
import gzip
from unittest.mock import MagicMock, patch
from bob_metric import lambda_handler

def test_lambda_handler():
    # Sample log event
    log_event = {
        "message": "@BotBot is in the thread, try to post message"
    }

    # Create a CloudWatch Logs event with the sample log event
    logs_data = {
        "logEvents": [log_event]
    }

    # Compress and encode the logs data
    compressed_logs_data = gzip.compress(json.dumps(logs_data).encode())
    encoded_logs_data = base64.b64encode(compressed_logs_data).decode()

    # Create a Lambda event with the encoded logs data
    lambda_event = {
        "awslogs": {
            "data": encoded_logs_data
        }
    }

    # Mock the CloudWatch client
    cloudwatch_mock = MagicMock()

    # Test the Lambda function
    with patch("boto3.client", return_value=cloudwatch_mock):
        response = lambda_handler(lambda_event, None)

    # Check if the custom metric was generated
    cloudwatch_mock.put_metric_data.assert_called_once()

    # Check the response
    assert response["statusCode"] == 200
    assert json.loads(response["body"]) == "Successfully processed logs and generated custom metrics."