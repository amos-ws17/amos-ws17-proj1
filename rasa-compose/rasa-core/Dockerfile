FROM python:3

RUN apt-get update && apt-get install -y git && \
    apt-get install -y build-essential

RUN git clone https://github.com/RasaHQ/rasa_core.git

WORKDIR /rasa_core

RUN pip install -r requirements.txt && pip install -e . && pip install klein && pip install rasa_nlu

