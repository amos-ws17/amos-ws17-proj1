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

  [1]: https://packaging.python.org/tutorials/installing-packages/ 
