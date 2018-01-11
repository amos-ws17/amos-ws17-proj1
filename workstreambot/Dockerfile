FROM amoschatbot/rasabase:latest

RUN mkdir scrum

ADD . /rasa_core/scrum

WORKDIR /rasa_core/scrum

RUN pip install -r requirements.txt

RUN python train.py -d scrum -n nlu_training_data_scrum.json

ENV FLASK_APP=http_service.py

ENTRYPOINT python -m flask run 
