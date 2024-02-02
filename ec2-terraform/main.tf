terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 5.25.0"
    }
  }

  required_version = ">= 1.5.7"
}

provider "aws" {
  region = "us-east-1"
}

resource "aws_instance" "app_server" {
  ami           = "ami-0cf10cdf9fcd62d37"
  instance_type = "t2.micro"

  tags = {
    Name = var.instance_name
  }
}

