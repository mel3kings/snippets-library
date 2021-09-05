# GIVEN:
```
daf34f48d13b   wurstmeister/kafka       "start-kafka.sh"         5 minutes ago   Up 5 minutes   0.0.0.0:9092->9092/tcp                               kafka
13bfe71dd1dd   wurstmeister/zookeeper   "/bin/sh -c '/usr/sb…"   5 minutes ago   Up 5 minutes   22/tcp, 2888/tcp, 3888/tcp, 0.0.0.0:2181->2181/tcp   zookeeper
```

## List Brokers
docker exec -ti kafka /usr/bin/broker-list.sh

## List Topics
docker exec -ti kafka /opt/kafka/bin/kafka-topics.sh --list --zookeeper zookeeper:2181

## Create a Topic
docker exec -ti kafka /opt/kafka/bin/kafka-topics.sh --create --zookeeper zookeeper:2181 --replication-factor 1 --partitions 1 --topic test2

## List Topics
docker exec -ti kafka /opt/kafka/bin/kafka-topics.sh --list --zookeeper zookeeper:2181



# Breakdown

zookeeper - zookeeper is in charge of leader election, and coordinating brokers

Generally Kafka usually run under a zookeeper, and won't work without one

Zookeeper makes sure that there is always a leader for the brokers, and monitors them

Kafka environment:

KAFKA_CREATE_TOPICS - creates a topic on startup with this format: <topic_name>:<no_of_partition>:<replication_factor>

Just by specifying replication factor, and with enough brokers, zookeeper handles the rest. This helps with your application's resiliency as it is not dependent in one messaging broker alone

KAFKA_ZOOKEEPER_CONNECT - which zookeeper to connect to

KAFKA_ADVERTISED_HOST_NAME - host name/ip

Second Kafka is named kafka_2

Notice that under ports, we use a different port number

and that we do note create the topic anymore under environment, but connects to the same zookeeper

Ensuring Replication is done:

./kafka-console-consumer.sh --bootstrap-server 192.168.99.100:9092 --topic first-topic --from-beginning

./kafka-console-consumer.sh --bootstrap-server 192.168.99.100:9093 --topic first-topic --from-beginning

NOTES: Even if we did not create the topic on the second kafka, we can list out the messages from the 2nd kafka service, this is because we have a replication factor of 2 when we created the topic. Zookeeper is then in charge of picking which kafka broker to replicate the topic to, and since we only have 2 brokers in this instance we can instantly find that the messages are replicated in both brokers.

Possible UI:

Topics UI
Schema UI
Connect UI
Kafka Manager
Burrow
Exhibitor
Kafka monitor
Kafka Tools
Kafkat