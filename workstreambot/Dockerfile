FROM amoschatbot/rasabase:latest

RUN mkdir workstreambot

ADD . /rasa_core/workstreambot

WORKDIR /rasa_core/workstreambot

RUN pip install -r requirements.txt

RUN python train.py -d scrum+kanban -n nlu_training_data_full.json

ENTRYPOINT python -m http_service -d scrum+kanban -t redis
