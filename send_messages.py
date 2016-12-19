#!/usr/bin/env python

import pika
import time


def send_message(host):
    queue_name = 'test_queue'
    vhost = 'pause'
    user = 'guest'
    password = 'guest'
    credentials = pika.PlainCredentials(user, password)
    parameters = pika.ConnectionParameters(
                    host=host,
                    virtual_host=vhost,
                    credentials=credentials)
    print 'Sending message to: {}'.format(host)
    try:
        connection = pika.BlockingConnection(parameters)
        channel = connection.channel()
        channel.queue_declare(queue=queue_name, exclusive=False)
        channel.basic_publish(exchange='',
                              routing_key=queue_name,
                              body='Hello {}'.format(host))
        channel.close()
    except pika.exceptions.ConnectionClosed:
        print 'Failed to send, ConnectionClosed'
    except pika.exceptions.ProbableAuthenticationError:
        print 'Failed to send, ProbableAuthenticationError'


if __name__ == "__main__":
    while True:
        send_message('172.21.21.11')
        send_message('172.21.21.12')
        send_message('172.21.21.13')
        time.sleep(10)
