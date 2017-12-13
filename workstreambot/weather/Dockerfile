FROM amoschatbot/rasabase:latest

RUN mkdir weather_bot

ADD . /rasa_core/weather_bot

WORKDIR /rasa_core/weather_bot

RUN pip install -r requirements.txt

RUN python -m rasa_nlu.train -c nlu_model_config.json --fixed_model_name current && python -m rasa_core.train -s data/stories.md -d domain.yml -o project/dialogue

ENTRYPOINT python -m rasa_core.run -d project/dialogue -u project/nlu/current -c cmdline
