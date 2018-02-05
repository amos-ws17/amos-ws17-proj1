# Conversational Chatbot

Conversational Chatbot (amos-ws17-pro1) is a project for the 2017 AMOS Course of the Technical University of Berlin in collaboration with the Actano GmbH ([actano.com](http://www.actano.com)) to give work teams a hand in agile methods related topics. The chat bot converses with the user about agile methods like Scrum and Kanban. It guides the user through the topics by giving him brief overview of the terminology used in those processes.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Deployment

To deploy the system make sure you have docker and git installed. If you do, clone this repository with:

```
git clone https://github.com/amos-ws17/amos-ws17-proj1.git
```

Then navigate to the newly created _amos-ws17-proj1_ folder and type in the following command to start deploy the bots:

```
docker-compose up
```

### Manual installation

Install a virtualenv in a desired location

```
sudo pip install virtualenv
# cd to our desired location
virtualenv -p python venv
```

Start your venv

```
source venv/bin/activate
```

Install Rasa NLU

```
pip install rasa_nlu
```

Install necessary libraries

```
pip install -U spacy
python -m spacy download en
pip install -U scikit-learn scipy sklearn-crfsuite
pip install flask
pip install -U pytest
```

Install Rasa Core

```
pip install rasa_core
```

For more details on installing Rasa take a look into the [Rasa NLU](http://nlu.rasa.ai/installation.html) and [Rasa Core](https://core.rasa.ai/installation.html) documentation.

### Train and run the service

Start your venv

```
# cd to our desired location
source venv/bin/activate
```

Train the models (in this case all)

```
# cd to amos-ws17/workstreambot
python -m train -d scrum+kanban -n nlu_training_data_full.json
```

Run the service

```
python -m http_service -d scrum+kanban
```

### Running the tests

Start your venv

```
# cd to our desired location
source venv/bin/activate
```

Train the models

```
# cd to amos-ws17/workstreambot
python -m train -d scrum+kanban -n nlu_training_data_full.json
```

Run the tests

```
python -m pytest test/ # execute all component tests
```

## Modify the dialogue

Due to the choice to use a micro service approach instead of a monolithic one the modification of the dialogue is much more simpler. It is possible to load different dialogue combinations during the start how this is done is explained in [Dialogue Topic Creation](https://github.com/amos-ws17/amos-ws17-proj1/wiki/Dialogue-Topic-Creation)

## Built With

* [Python](https://docs.python.org/3/) - Python 3 Documentation
* [Rasa NLU](https://nlu.rasa.ai/index.html) - Rasa NLU Documentation
* [Rasa Core](https://core.rasa.ai/index.html) - Rasa Core Documentation

## Contributing

* **Billie Thompson** - *Readme Template* - [PurpleBooth](https://github.com/PurpleBooth)


## Versioning

For the versions available, see the [tags on this repository](https://github.com/amos-ws17/amos-ws17-proj1/tags). 

## Authors

* Lukas Kleine Büning
* Etjen Ymeraj 
* Daniel Dimitrov
* Radoslav Vlaskovski 
* Veselin Popov
* Omar Abada
* Marah Halawa

See also the contributing section

## License

This project is licensed under the Apache 2.0 License - see the [LICENSE](LICENSE) file for details
