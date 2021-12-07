resource "local_file" "pet"{
  content="we love pets"
  filename= var.filename
  file_permission="0700"
}
