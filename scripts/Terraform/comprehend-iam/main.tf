provider "aws" {
  region = "ap-southeast-2"
}

resource "aws_iam_user" "comprehend_user" {
  name = "comprehend_user"
  path = "/system/"

  tags = {
    tag-key = "tag-value"
  }
}

resource "aws_iam_access_key" "comprehend_user" {
  user = aws_iam_user.comprehend_user.name
}

resource "aws_iam_user_policy" "comprehend_user_ro" {
  name = "test"
  user = aws_iam_user.comprehend_user.name
  policy = file("comprehend-policy.json")
}


data "template_file" "secret" {
  template = aws_iam_access_key.comprehend_user.secret
}

output "brand_new_user_secret" {
  value     = data.template_file.secret.rendered
}

output "user" {
  value = aws_iam_access_key.comprehend_user.user
}
