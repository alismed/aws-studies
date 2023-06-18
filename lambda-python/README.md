## AWS Lambda Function

It's a hello world using python

### It's necessary:
- Sign up for an AWS account
- AWS Cli configured
- Python
- Terraform

Initialize the terraform project
```shell
terraform init
```

### Deploy
```shell
terraform plan

terraform apply
```

To destroy, use:
```shell
terraform apply -destroy
```

### Test
It's possible to execute no complex tests, running lambda function on local machine.
```shell
pip install python-lambda-local
```

And execute the command below
```shell
python-lambda-local -f lambda_handler src/index.py spec/event.json
```

Also use the AWS console to test

