FROM python:3

RUN apt-get update && apt-get install -y git && \
    apt-get install -y build-essential && apt-get install -y default-jre

RUN git clone https://github.com/RasaHQ/rasa_core.git

WORKDIR /rasa_core

RUN pip install -r requirements.txt && pip install -e . && pip install klein && pip install rasa_nlu &&\
    pip install spacy sklearn sklearn_crfsuite && python -m spacy download en && pip install flask

RUN mkdir weather_bot

ADD . /rasa_core/weather_bot

WORKDIR /rasa_core/weather_bot

RUN pip install -r requirements.txt

RUN python -m rasa_nlu.train -c nlu_model_config.json --fixed_model_name current && python -m rasa_core.train -s data/weather_stories.md -d weather_domain.yml -o project/dialogue

ENTRYPOINT python -m rasa_core.server -d mod/dialogue -u project/nlu/current
