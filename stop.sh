#!/bin/bash
python stop.py
sleep 2
#docker stop rabbit
docker rm $(docker ps -q -f "status=exited")
#docker rm rabbit

