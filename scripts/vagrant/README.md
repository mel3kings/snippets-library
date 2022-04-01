# What is it?
- For spinning up quickly custom infrastructure on your local (e.g Linux, Windows Machine etc)
- Ubuntu + Nginx

# Prerequisites
- Have Vagrant (+VirtualBox if Mac) in your local machine

# How to Start
- in the terminal, where Vagrantfile is located run `Vagrant up`
- `Vagrant destroy` to delete

# NOTES
- update node
- install nginx: sudo apt install nginx

check firewall:
- check status: sudo ufw app list
- sudo ufw allow 'Nginx HTTP'
- check status: sudo ufw status


configure nginx:
- get server ip should default a home page
- update: /etc/nginx/sites-enabled
  location / {
  # First attempt to serve request as file, then
  # as directory, then fall back to displaying a 404.
  # try_files $uri $uri/ =404;
  proxy_pass http://127.0.0.1:7777/;
  }
- add default.conf
- restart nginx
