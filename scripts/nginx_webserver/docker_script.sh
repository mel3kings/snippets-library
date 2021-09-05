#!/bin/bash
yum install docker -y
yum update -y
service docker start

# MANUAL RUN
# sudo su
# sudo yum install -y docker
# service docker start