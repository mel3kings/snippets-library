module "s3_bucket" {
  source             = "cloudposse/s3-bucket/aws"
  # Cloud Posse recommends pinning every module to a specific version
  version            = "3.0.0"
  name               = "rekognition-mel3kings"
  stage              = "test"
  namespace          = "eg"
  acl                = "private"
  enabled            = true
  versioning_enabled = false
  # Create user
  user_enabled       = true
  access_key_enabled = true
  privileged_principal_actions = ["s3:GetObject", "s3:ListBucket", "s3:GetBucketLocation", "s3:*"]
  policy                       = <<EOF
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "AddPerm",
            "Effect": "Allow",
            "Principal": "*",
            "Action": "s3:*",
            "Resource": "arn:aws:s3:::rekognition-mel3kings/*"
        }
    ]
}
EOF
}


