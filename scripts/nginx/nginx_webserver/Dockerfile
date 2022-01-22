# this same shows how we can extend/change an existing official image from Docker Hub

FROM nginx:latest
# highly recommend you always pin versions for anything beyond dev/learn

WORKDIR /usr/share/nginx/html
# change working directory to root of nginx webhost using WORKDIR is prefered to using 'RUN cd /some/path'

COPY bashscript.sh bashscript.sh
RUN ["chmod", "+x", "./bashscript.sh"]
RUN ["./bashscript.sh"]

COPY index.html index.html
COPY .htpasswd /etc/nginx/.htpasswd
RUN ["chmod", "644", "/etc/nginx/.htpasswd"]

COPY nginx.conf /etc/nginx/conf.d/default.conf
COPY test.png /data/images/test.png
# I don't have to specify EXPOSE or CMD because they're in my FROM
