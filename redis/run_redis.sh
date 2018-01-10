#!/bin/bash

docker run --name redis-container -p 6379:6379 --expose 6379 -d redis