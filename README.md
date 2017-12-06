# Conversational Chatbot

A project for the 2017 AMOS Course in collaboration with Actano

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
Now all bots are running and are accesssible on those ports:
* **Weather bot:** 5012, 5015, 5010
* **Sightseeing bot:** 5022, 5025, 5020
* **Restaurant bot:** 5032

### Manual installation and deployment

Install a virtualenv in a desired location

```
sudo pip install virtualenv
#cd to our desired location
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
pip install requests 
pip install -U spacy
python -m spacy download en
pip install -U scikit-learn scipy sklearn-crfsuite
python -m pip install duckling
```

Install Rasa Core

```
pip install rasa_core
```

Now you should be able to run the [weather bot](https://github.com/amos-ws17/amos-ws17-proj1/wiki/Weather-bot).  
For more details on installing Rasa take a look into the [Rasa NLU](http://nlu.rasa.ai/installation.html) and [Rasa Core](https://core.rasa.ai/installation.html) documentation.

## Running the tests

Explain how to run the automated tests for this system

### Break down into end to end tests

Explain what these tests test and why

```
Give an example
```

### And coding style tests

Explain what these tests test and why

```
Give an example
```

## Models

* [Weather Model](https://github.com/amos-ws17/amos-ws17-proj1/wiki/Weather-bot) whose data is provided by [Yahoo](https://developer.yahoo.com/weather/documentation.html) - Weather API Documentation

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

## Acknowledgments

* Hat tip to anyone who's code was used
* Inspiration
