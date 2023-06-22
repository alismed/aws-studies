## Api Gateway and Lambda with Python



```shell
terraform -chdir="./infra" init
```

Initialize the terraform project
```shell
terraform -chdir="./infra" init
```

### Deploy
```shell
terraform -chdir="./infra" plan
terraform plan

terraform -chdir="./infra" apply
```

To destroy, use:
```shell
terraform -chdir="./infra" apply -destroy
```

### Test
It's possible to execute no complex tests, running lambda function on local machine.
```shell
pip install python-lambda-local
```

And execute the command below
```shell
python-lambda-local -f lambda_handler src/main.py spec/event.json
```

