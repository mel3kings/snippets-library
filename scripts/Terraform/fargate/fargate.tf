
#resource "aws_ecs_cluster" "cluster" {
#  name = "example-ecs-cluster"
#
#  capacity_providers = ["FARGATE_SPOT", "FARGATE"]
#
#  default_capacity_provider_strategy {
#    capacity_provider = "FARGATE_SPOT"
#  }
#
#  setting {
#    name  = "containerInsights"
#    value = "disabled"
#  }
#}

#resource "aws_subnet" "main" {
#  vpc_id     = aws_vpcvpc.main.id
#  cidr_block = "10.0.1.0/24"
#
#  tags = {
#    Name = "Main"
#  }
#}

#
#module "ecs-fargate" {
#  source  = "umotif-public/ecs-fargate/aws"
#  version = "~> 6.1.0"
#
#  name_prefix        = "ecs-fargate-example"
#  vpc_id             = vpc.public_vpc.id
## private_subnet_ids = ["subnet-abasdasd132123", "subnet-abasdasd132123132"]
#
#  cluster_id = aws_ecs_cluster.cluster.id
#
#  task_container_image   = "marcincuber/2048-game:latest"
#  task_definition_cpu    = 256
#  task_definition_memory = 512
#
#  task_container_port             = 80
#  task_container_assign_public_ip = true
#
#  target_groups = [
#    {
#      target_group_name = "tg-fargate-example"
#      container_port    = 80
#    }
#  ]
#
#  health_check = {
#    port = "traffic-port"
#    path = "/"
#  }
#
#  tags = {
#    Environment = "test"
#    Project     = "Test"
#  }
#}