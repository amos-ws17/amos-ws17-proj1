FROM python:3

RUN apt-get update && apt-get install -y git && \
    apt-get install -y build-essential

RUN git clone https://github.com/RasaHQ/rasa_core.git

WORKDIR /rasa_core

RUN pip install -r requirements.txt && pip install -e . && pip install klein && pip install rasa_nlu &&\
    pip install spacy sklearn sklearn_crfsuite && python -m spacy download en && pip install flask

ENV DATA_SRC moodbot
WORKDIR /rasa_core/examples/${DATA_SRC}

RUN python -m rasa_nlu.train -c nlu_model_config.json --fixed_model_name current && python -m rasa_core.train -s data/stories.md -d domain.yml -o models/dialogue

ENTRYPOINT python -m rasa_core.server -d models/dialogue -u models/nlu/current
