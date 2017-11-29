#!/bin/bash

set -ex

# Release script for the bots

# Version for tagging
version=`cat VERSION`
echo "version: $version"

# Build bots

docker build -t amoschatbot/weatherbot:$version weather/
docker build -t amoschatbot/sightseeingbot:$version sightseeing/
docker build -t amoschatbot/restaurantbot:$version restaurant/

docker push amoschatbot/weatherbot:$version
docker push amoschatbot/sightseeingbot:$version
docker push amoschatbot/restaurantbot:$version

# Tag release 
#git tag -a "$version" -m "version: $version"
#git push --tags
