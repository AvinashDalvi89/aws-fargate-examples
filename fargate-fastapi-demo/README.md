# FastAPI on AWS Fargate with New Relic Integration

This project demonstrates how to deploy a FastAPI application on AWS Fargate with New Relic monitoring.

## Project Structure

- `main.py` - FastAPI application
- `Dockerfile` - Original Dockerfile
- `Dockerfile.newrelic` - Dockerfile with New Relic agent integration
- `requirements.txt` - Original dependencies
- `requirements.newrelic.txt` - Dependencies including New Relic
- `fargate-cfn.yaml` - CloudFormation template for Fargate deployment

## Deployment Steps

1. **Build and push the Docker image**

   ```bash
   # Update to the New Relic version of the application
   cp main.py.newrelic main.py
   cp requirements.newrelic.txt requirements.txt
   cp Dockerfile.newrelic Dockerfile
   
   # Create an ECR repository (if not already created)
   aws ecr create-repository --repository-name fastapi-demo
   
   # Build and push the Docker image
   aws ecr get-login-password --region <your-region> | docker login --username AWS --password-stdin <your-account-id>.dkr.ecr.<your-region>.amazonaws.com
   docker build -t <your-account-id>.dkr.ecr.<your-region>.amazonaws.com/fastapi-demo:latest .
   docker push <your-account-id>.dkr.ecr.<your-region>.amazonaws.com/fastapi-demo:latest
   ```

2. **Deploy the CloudFormation stack**

   ```bash
   aws cloudformation create-stack \
     --stack-name fastapi-newrelic-demo \
     --template-body file://fargate-cfn.yaml \
     --parameters \
       ParameterKey=NewRelicLicenseKey,ParameterValue=<your-new-relic-license-key> \
       ParameterKey=NewRelicAppName,ParameterValue=FastAPI-Demo \
     --capabilities CAPABILITY_IAM
   ```

3. **Monitor the deployment**

   ```bash
   aws cloudformation describe-stacks --stack-name fastapi-newrelic-demo
   ```

4. **Access the application**

   Once the deployment is complete, you can access the application using the LoadBalancer DNS name from the CloudFormation outputs.

## New Relic Integration

The New Relic agent is integrated in the following ways:

1. The New Relic Python agent is installed in the Docker container
2. Environment variables for New Relic configuration are passed through the ECS task definition
3. The application is started with the New Relic admin script
4. The main.py file initializes the New Relic agent

## Testing the Application

The application includes several endpoints for testing:

- `/` - Returns a simple greeting message
- `/error` - Triggers a simulated error (for testing error reporting)
- `/slow` - Returns a response after a random delay (for testing performance monitoring)

These endpoints will be automatically monitored by New Relic, providing insights into application performance and errors.
