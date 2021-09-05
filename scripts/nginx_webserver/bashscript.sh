#!/bin/bash
yum install httpd -y
yum update -y
service httpd start
chkconfig httpd on


