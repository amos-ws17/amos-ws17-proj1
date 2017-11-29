#!/bin/bash

set -ex

# Release script for the bots

# Ensure we're up to data
git pull

# Version for tagging
version=`cat VERSION`
echo "version: $version"

# Build bots

docker build -t amoschatbot/weatherbot:$version weather/
docker build -t amoschatbot/sightseeingbot:$version sightseeing/

docker push amoschatbot/weatherbot:$version
docker push amoschatbot/sightseeingbot:$version

# Tag release 
#git tag -a "$version" -m "version: $version"
#git push --tags


