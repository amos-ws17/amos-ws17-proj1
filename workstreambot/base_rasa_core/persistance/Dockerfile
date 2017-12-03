FROM python:3

RUN apt-get update -y && pip install pymongo && mkdir persistance

WORKDIR persistance

ADD . .

ENTRYPOINT python
