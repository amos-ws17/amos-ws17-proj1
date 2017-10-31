----------

RASA Core - Supervised learning tutorial
-------------

In this example we will create a restaurant search bot, by training a neural net on example conversations. A user can contact the bot with something close to "I want a mexican restaurant!" and the bot will ask more details until it is ready to suggest a restaurant.
Let's start by cloning the [Github repository of RASA Core] [1] somewhere on the hard disk. After that we should create an examples/ directory
in Python36/Lib/site-packages/. The project folder of the restaurant search bot is in the rasa_core/examples/ directory of the cloned
RASA Core Github repository. Copy the folder restaurantbot/ in Python36/Lib/site-packages/examples/.

**1. Creating the Domain**

Our restaurant domain contains a couple of slots as well as a number of intents, entities, utterance templates and actions.
The domain definition for this example is already in the folder restaurantbot/, which we copied from the Github repository of RASA Core.

Our Domain has clearly defined **slots** (in our case criterion for target restaurant) and **intents** (what the user can send).
It also requires **templates** to have text to use to respond given a certain **action**.

Each of these **actions** must either be named after an utterance (dropping the **utter_** prefix) or must be a module path to an action. 
Here is the code for one of the two custom actions:

	from rasa_core.actions import Action

	class ActionSearchRestaurants(Action):
		def name(self):
			return 'search_restaurants'

		def run(self, dispatcher, tracker, domain):
			dispatcher.utter_message("here's what I found")
			return []
			
The **name** method is to match up actions to utterances, and the **run** command is run whenever the action is called. 
This may involve api calls or internal bot dynamics.

But a domain alone doesn’t make a bot, we need some training data to tell the bot which actions it should execute at what point in time. 
So lets create some stories!

**2. Creating Training Data**

The training data for this example is located in restaurantbot/data/babi_stories.md .Here’s an example conversation snippet:

	## story_07715946
	* _greet[]
	 - action_ask_howcanhelp
	* _inform[location=rome,price=cheap]
	 - action_on_it
	 - action_ask_cuisine
	* _inform[cuisine=spanish]
	 - action_ask_numpeople
	* _inform[people=six]
	 - action_ack_dosearch
	 ...

**3. Training your bot**

We can go directly from data to bot with only a few steps:

1. train a Rasa NLU model to extract intents and entities. Read more about that in the NLU docs.
2. train a dialogue policy which will learn to choose the correct actions.

**NLU model**
To train our Rasa NLU model, we need to create a configuration first. This configuration is already present in
the restaurantbot/nlu_model_config.json.

We can train the NLU model using

	python -m rasa_nlu.train -c nlu_model_config.json --fixed_model_name current
	
This line must be called from the examples/restaurantbot/ folder.

**Dialogue Policy**

Now our bot needs to learn what to do in response to these messages. We do this by training one or multiple Rasa Core policies.
We use the policy that is already defined in the bot.py script inside of restaurantbot/. The policy itself is represented by
the class RestaurantPolicy. The function train_dialogue in the bot.py is used to train the policy. To train the dialogue policy
from command prompt, run

	python bot.py train-dialogue
	
This line must be called from the examples/restaurantbot/ folder.

**4. Start the trained bot**

In order to start the trained bot you need to run

	python bot.py run
	
This line must be called from the examples/restaurantbot/ folder.

----------

  [1]: https://github.com/RasaHQ/rasa_core