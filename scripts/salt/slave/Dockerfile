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
# minion commands
COPY minion /etc/salt/
COPY run_me.sh /etc/salt
COPY run_me2.sh /etc/salt
COPY cm_deploy.py /etc/salt
RUN chmod 777 /etc/salt/run_me.sh
RUN chmod 777 /etc/salt/run_me2.sh
RUN chmod 777 /etc/salt/run.py
RUN echo 'DONE'
CMD ["salt-minion", "-l", "debug"]
