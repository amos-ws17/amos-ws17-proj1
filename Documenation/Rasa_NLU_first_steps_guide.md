Installation
===================
Here we will explain how to install Rasa NLU in a simple way.

----------

Pip
-------------
It is highly recommended to install “pip” which is a tool for installing python packages. It can detect the dependencies for any library you would like to install. Example of installing a library using pip:
 pip install <name_of_library>
As simple as that. To install pip if you don’t have it, please check [This][1] .
However, it must be installed by default if you have python you have Python 2 >=2.7.9 or Python 3 >=3.4 installed.

----------


Virtualenv
-------------------
When using pip, by default all the installed libraries will be installed into “site-packages” folder inside your python directory. This means that all libraries and dependencies you install, will be inside the same folder. It is dangerous sometimes to install all libraries into this folder, as it may cause conflicts of versions. In addition, some libraries would require root permissions to be installed.

Thus, it is highly recommended to use the virtualenv tool, which will create a separate folder for all your python libraries and dependencies. This virtual environment is an isolated location which can even be created for each of your projects. However, you can use the same Venv for multiple similar projects. 

**To install venv, use the following command:**

    sudo pip install virtualenv

**To create a new virtual environment:** (please make sure to “cd” to your desired location of the venv) 

    virtualenv -p python venv

> **Note:**
Please note that the word “venv” is the name of your created virtualenv, you can choose whatever name you want. E.g. to be able to create multiple ones. Please also note that there is a python interpreter inside this venv, which will be used when you run this venv.

**To activate the created venv, use the following command:**

    source venv/bin/activate

This will run your venv, and this will use the python version inside this venv. And also will use the pip version in this venv. So, voilà, now all the consequent pip installations will be in this venv. Just call “pip install <library>”. Do not forget to activate your venv before running python projects later.

----------
Rasa NLU
-------------------
**The recommended way to install rasa NLU is using pip:**

    pip install rasa_nlu

----------

Setting up a backend 
-------------------
To use Rasa NLU, we have to install on of these library (MITIE, spaCy, sklearn). It is highly recommended to install spaCy + sklearn.
	> **Note:**
> - spaCy is a natural language processing library in python.
> - sklearn is a machine learning library in python.

**To install spacy use the following commands:**

    pip install -U spacy

    python -m spacy download en


**To install sklearn use the following command:**
	

    pip install -U scikit-learn scipy sklearn-crfsuite


----------

RASA NLU on HTTP server
-------------

First let's see what our config_spacy.json file looks like:

    {
      "pipeline": "spacy_sklearn",
      "path" : "./projects",
      "data" : "./model-sample.json"
    }

"pipeline" is used for training. It can either be a template (passing a string) or a list of components (array). Later we would add one more pipeline just to fiddle with it.
"path" shows us the projects directory where trained models will be saved to (training) and loaded from (http server).
"data" shows us where the defined model is located. A very useful tool to create or explore an existing model is [this tool][3]. Later this tool can be used to manually make the models for the workstreams slack app.

Now open the command prompt and go to the directory where the config_spacy.json file is located. To be able to test the system, we first have to have a trained it:

    python -m rasa_nlu.train -c config_spacy.json

That would create two folders in the "path" directory specified in the config_spacy.json file, namely - 'log' and 'projects'.

To start the HTTP server just do:

    python -m rasa_nlu.server -c config_spacy.json

Now we have a server running and can see what it can do. To test the API that the RASA server offers download [cURL][2] to test out the API. For Windows just unzip it and add the path to curl.exe in the enironment variables.

For Windows do 

    curl "localhost:5000/parse?q=I%20am%20looking%20for%20Chinese%20food" | python -mjson.tool

instead of

    curl -XPOST localhost:5000/parse -d '{"q":"I am looking for Chinese food"}' | python -mjson.tool

because windows has a problem with the quotation marks.
If everything is working as it should be we should get back:

    {
        "intent": {
            "name": "restaurant_search",
            "confidence": 0.8467755965756901
        },
        "entities": [],
        "intent_ranking": [
            {
                "name": "restaurant_search",
                "confidence": 0.8467755965756901
            },
            {
                "name": "goodbye",
                "confidence": 0.0739631383246023
            },
            {
                "name": "greet",
                "confidence": 0.04713317467404759
            },
            {
                "name": "affirm",
                "confidence": 0.032128090425659936
            }
        ],
        "text": "I am looking for Chinese food"
    }


To train / retrain the project throught the API do:

    curl -XPOST localhost:5000/train?project=default -d @model-sample-updated.json

Which would give the project the 'model-sample-updated.json' from which the program would train a new model.


----------

Entity extraction
-------------

With the setup up until now we can extract some information via the model we've defined in the "model-sample.json" file. But ofter we want to take some entities that are used quite often and are to various for us to define them all on our know. For example: Places, Dates, People, Organisations, Dates, Amounts of Money, Durations, Distances, Ordinals and others.

One such entity that we might have to use for the workstreams app is the date. For example to set until when is a specific task due. This can be said in many ways like for e.g.: "due to the first Tuesday of October", "after two days" or with the exact date "03.10.2017". One such library is the duckling library for python. Install it via pip:

    python -m pip install duckling

or if you are on Linux just:

    pip install duckling

After that add it to the pipeline in the config file:

    {
      "pipeline": ["nlp_spacy", 
        "tokenizer_spacy", 
        "intent_featurizer_spacy", 
        "intent_entity_featurizer_regex", 
        "ner_crf", 
        "ner_synonyms", 
        "intent_classifier_sklearn",
        "ner_duckling"],
      "path" : "./projects",
      "data" : "./model-sample.json"
    }

"ner_duckling" is the new component. All the other entries in the pipeline array are the components that were part of "spacy_sklearn" in our older version of the config file.
Now if we do:

    curl "localhost:5000/parse?q=I%20am%20going%20the%20first%20Tuesday%20of%20October" | python -mjson.tool

we get:

    {
        "intent": {
            "name": "restaurant_search",
            "confidence": 0.4791107815072393
        },
        "entities": [
            {
                "start": 15,
                "end": 20,
                "value": "first",
                "entity": "location",
                "extractor": "ner_crf"
            },
            {
                "start": 15,
                "end": 20,
                "text": "first",
                "value": 1,
                "additional_info": {
                    "value": 1
                },
                "entity": "ordinal",
                "extractor": "ner_duckling"
            },
            {
                "start": 11,
                "end": 39,
                "text": "the first Tuesday of October",
                "value": "2017-10-03T00:00:00.000Z",
                "additional_info": {
                    "value": "2017-10-03T00:00:00.000Z",
                    "grain": "day",
                    "others": []
                },
                "entity": "time",
                "extractor": "ner_duckling"
            }
        ],
        "intent_ranking": [
            {
                "name": "restaurant_search",
                "confidence": 0.4791107815072393
            },
            {
                "name": "goodbye",
                "confidence": 0.29204150043130345
            },
            {
                "name": "greet",
                "confidence": 0.16219173638109563
            },
            {
                "name": "affirm",
                "confidence": 0.0666559816803618
            }
        ],
        "text": "I am going the first Tuesday of October"
    }

Notice that each entry has an "extractor", which tells us which component in the pipeline extracted it.

----------

  [1]: https://packaging.python.org/tutorials/installing-packages/ 
  [2]: https://curl.haxx.se/download.html
  [3]: https://rasahq.github.io/rasa-nlu-trainer/