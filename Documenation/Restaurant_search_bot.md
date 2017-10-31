Restaurant search bot
===================
Here we will explain how to train Rasa NLU on restaurant search dataset.

----------

Preparing the Training Data
-------------

Collecting training data is the essential task has to be done when we work on machine learning models; we need a dataset to train a model on it. In our case the machine learning model is a supervised model, thus we need a labeled data set, these labels come from what we want from machine to learn. In restaurant search bot example we have three intents which are (greet, restaurant_search, thank you), thus the model should categorise each sentence to have one of these intents, and also we have two labels for words such as "cuisine", and "location". The model should also be able to assign words to these labels. Each sample from the dataset is a text such as "show me Chinese restaurants", and the labels are the intent such as "restaurant_search", and the entities such as "cuisine" is "Chinese". All this information is provided by a Json file.


> **Note:**
When we will choose our training data we have to insure that the dataset is composed of small-talk sentences, and we have to define our entities and intents.
You can see the training data format [here][1]

For this example, RASA NLU provides "demo-rasa.json" file, in the "data" folder. After that I installed Rasa NLU, then I cloned the project to be able to use their functions and data.

----------


Training a New Model for your Project
-------------------
First, we’re going to create a configuration file called "config_spacy.json"

    {
      "pipeline": "spacy_sklearn",
      "path" : "./projects",
      "data" : "./data/examples/rasa/demo-rasa.json"
    }

Now we can train a Spacy model by running:

     $ python -m rasa_nlu.train -c sample_configs/config_spacy.json

> **Note:**
We have to keep in our mind that when we install a python package we should use venv. 

After a few minutes, rasa NLU will finish training, and you’ll see a new folder (in default folder) named as 

    projects/default/model_YYYYMMDD-HHMMSS

This is our training model, which we will make an inference on.

> **Note:**
To train a new model for a new chatbot we may need to change some parameters in the training command above, that will depend on the results. All available parameters are provided [here][2].

----------

Using the Model
-------------------
By default, the server will look for all project folders under the path directory specified in the configuration. When no project is specified, as in this example, a “default” one will be used, itself using the latest trained model.

    $ python -m rasa_nlu.server -c sample_configs/config_spacy.json

**Test the model**
We can then test our new model by sending a request. Open a new tab/window on your terminal and run the following command:

    $ curl -XPOST localhost:5000/parse -d '{"q":"I am looking for Chinese food"}' | python -mjson.tool

The result will be the entities and intents for the text "I am looking for Chinese food".
Rasa NLU will also print a confidence value for the intent classification. For models using Spacy intent classification this will be a probability. We can use this to do some error handling in your chatbot (e.g. asking the user again if the confidence is low) and it’s also helpful for prioritising which intents need more training data.

----------

  [1]: http://rasa-nlu.readthedocs.io/en/latest/dataformat.html#section-dataformat
  [2]: http://rasa-nlu.readthedocs.io/en/latest/config.html#section-configuration
