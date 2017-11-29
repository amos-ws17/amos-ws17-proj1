FROM amoschatbot/rasabase:latest

RUN mkdir sightseeing_bot

ADD . /rasa_core/sightseeing_bot

WORKDIR /rasa_core/sightseeing_bot

RUN python -m rasa_nlu.train -c nlu_model_config.json --fixed_model_name current && python -m rasa_core.train -s data/stories.md -d domain.yml -o models/dialogue --epochs 300

ENTRYPOINT python -m rasa_core.run -d models/dialogue -u models/nlu/current -c bot
