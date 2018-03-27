#!/usr/bin/env bash

if [ -z "$1" ]
  then
    echo "Usage: ./start.sh <RabbitMQ_host>"
    exit
fi

for dir in Splitter Expander Ranker Tiler Results; do
	echo "Starting $dir"
	cd $dir
	python service.py $1 &
	cd -
done 
echo "Services started"
