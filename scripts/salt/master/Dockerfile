FROM ubuntu
RUN apt-get update && apt-get install -y \
    curl \
    sudo \
    iputils-ping \
    nano \
    vim
RUN curl -o bootstrap-salt.sh -L https://bootstrap.saltstack.com
RUN chmod 777 bootstrap-salt.sh
RUN ./bootstrap-salt.sh -M
# master commands
COPY master /etc/salt/
#COPY cm_deploy.py /etc/salt/
CMD ["salt-master", "-l", "debug"]
