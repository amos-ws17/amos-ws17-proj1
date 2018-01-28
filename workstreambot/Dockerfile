FROM amoschatbot/rasabase:latest

RUN mkdir bot

ADD . /rasa_core/bot

WORKDIR /rasa_core/bot

RUN pip install -r requirements.txt

RUN python train.py -d scrum+kanban -n nlu_training_data_full.json

ENTRYPOINT python -m http_service -d scrum+kanban -t redis
