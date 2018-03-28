#!/bin/bash

if [ -z "$1" ]; then
    HOST=172.17.0.2
else
    HOST=$1
fi

for dir in splitter expander ranker tiler results; do
	echo "Starting $dir, host $HOST"
    docker run -td -v /tmp:/tmp --name $dir bioasq/$dir $HOST
done 

echo "Services started"
