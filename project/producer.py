from confluent_kafka import Producer


def produce_message(data_source: list):
    p = Producer({'bootstrap.servers': 'localhost'})

    def delivery_report(err, msg):
        """ Called once for each message produced to indicate delivery result.
            Triggered by poll() or flush(). """
        if err is not None:
            print('Message delivery failed: {}'.format(err))
        else:
            print('Message delivered to {} [{}]'.format(msg.topic(), msg.partition()))

    for data in data_source:
        # Trigger any available delivery report callbacks from previous produce() calls
        # p.poll(1)

        # Asynchronously produce a message, the delivery report callback
        # will be triggered from poll() above, or flush() below, when the message has
        # been successfully delivered or failed permanently.
        p.produce('mytopic', data.encode('utf-8'), callback=delivery_report)

    # Wait for any outstanding messages to be delivered and delivery report
    # callbacks to be triggered.
    p.flush()


if __name__ == '__main__':  # pragma: no cover
    produce_message(["test{}".format(i) for i in range(10)])
