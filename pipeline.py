#!/usr/bin/env python

import sys
from deiis.rabbit import Message, MessageBus
from deiis.model import Serializer, DataSet, Question

if __name__ == '__main__':
    if len(sys.argv) <= 2:
        print 'Usage: python pipeline.py <data.json> <RabbitMQ_host>'
        exit(1)

    # filename = 'data/training.json'
    filename = sys.argv[1]
    print 'Processing ' + filename
    fp = open(filename, 'r')
    dataset = Serializer.parse(fp, DataSet)
    fp.close()

    # The list of services to send the questions to.
    rabbit_host = sys.argv[2]
    #pipeline = ['mmr.core', 'tiler.concat', 'results']
    pipeline = ['splitter', 'mmr.core', 'tiler.concat', 'results']
    count=0
    bus = MessageBus(host = rabbit_host)
    for index in range(0,10):
        question = dataset.questions[index]
    # for question in dataset.questions:
        message = Message(body=question, route=pipeline)
        bus.publish('expand.none', message)
        count = count + 1

    print 'Sent {} questions for ranking.'.format(count)
    print 'Done.'
