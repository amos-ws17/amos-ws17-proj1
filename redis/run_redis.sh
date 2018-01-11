#!/bin/bash

docker run --name redis-container  --network redis-network -p 6379:6379 --expose 6379 -d redis
