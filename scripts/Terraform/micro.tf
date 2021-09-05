provider "aws" {
  access_key = "AKIAIQYIP3YEMWQV6D2Q"
  secret_key = ""
  region     = "ap-southeast-2"
}

resource "aws_instance" "example" {
  ami           = "ami-43874721"
  instance_type = "t2.micro"
  subnet_id ="subnet-173e565e"
}