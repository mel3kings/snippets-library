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

