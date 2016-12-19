#!/usr/bin/env python

import pika

if __name__ == "__main__":
    exchange_name = 'test_exchange'
    queue_name = 'test_queue'
    host = '172.21.21.11'
    vhost = 'pause'
    user = 'guest'
    password = 'guest'
    credentials = pika.PlainCredentials(user, password)
    parameters = pika.ConnectionParameters(
                    host=host,
                    virtual_host=vhost,
                    credentials=credentials)
    connection = pika.BlockingConnection(parameters)
    channel = connection.channel()
    result = channel.queue_declare(queue=queue_name, exclusive=False)

    def callback(ch, method, properties, body):
        print(" [x] Received %r" % body)

    channel.basic_consume(callback,
                          queue=queue_name,
                          no_ack=True)

    print(' [*] Waiting for messages. To exit press CTRL+C')
    channel.start_consuming()
