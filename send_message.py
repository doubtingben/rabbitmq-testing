#!/usr/bin/env python

import pika

if __name__ == "__main__":
    exchange_name = 'test_exchange'
    queue_name = 'test_queue'
    host = '172.21.21.11'
    vhost = 'my_vhost'
    user = 'test'
    password = 'test'
    credentials = pika.PlainCredentials(user, password)
    parameters = pika.ConnectionParameters(
                    host=host,
                    virtual_host=vhost,
                    credentials=credentials)
    connection = pika.BlockingConnection(parameters)
    channel = connection.channel()
    result = channel.queue_declare(queue=queue_name, exclusive=False)
    channel.basic_publish(exchange='',
                          routing_key=queue_name,
                          body='Hello World!')
