FROM python:3

RUN apt-get update && apt-get install -y git && \
    apt-get install -y build-essential && apt-get install -y default-jre

RUN git clone https://github.com/RasaHQ/rasa_core.git -b 0.7.8

WORKDIR /rasa_core

RUN pip install -e . && pip install klein && pip install rasa_nlu &&\
    pip install spacy sklearn sklearn_crfsuite && python -m spacy download en && pip install flask && pip install -U pytest

ADD . rasa_core/
