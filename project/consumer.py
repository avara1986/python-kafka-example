from confluent_kafka import Consumer, KafkaError

c = Consumer({
    'bootstrap.servers': 'localhost',
    'group.id': 'mygroup',
    'default.topic.config': {
        'auto.offset.reset': 'smallest'
    }
})
# topic = TopicPartition('mytopic', 0)
c.subscribe(['mytopic'])


def get_data():
    print("check if data")
    msg = c.poll(1.0)
    return msg


if __name__ == '__main__':  # pragma: no cover
    try:
        while True:
            msg = get_data()

            if msg is None:
                continue
            if msg.error():
                if msg.error().code() == KafkaError._PARTITION_EOF:
                    continue
                else:
                    print(msg.error())
                    break

            print('Received message: {}'.format(msg.value().decode('utf-8')))
    except KeyboardInterrupt:
        pass
    print("cerrando sesión")
    c.close()
