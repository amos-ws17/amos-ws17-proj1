----------

RASA Core - HTTP Server
-------------

Before you can use the server, you need to define a domain, create training data, and train a model. 
You can then use the trained model for remote code execution! See [Building a Simple Bot][1] for an introduction.

**Overview**

The general idea is to run the actions within your code (arbitrary language), instead of python. 
To do this, Rasa Core will start up a web server where you need to pass the user messages to. 
Rasa Core on the other side will tell you which actions you need to run. 
After running these actions, you need to notify the framework that you executed them and tell the model about 
any update of the internal dialogue state for that user. All of these interactions are done using a HTTP REST interface.

To activate the remote mode, include

	action_factory: remote
	
within your domain.yml in path/Lib/site-packages/examples/moodbot. When you add the **action_factory** you need to train the NLU model and the
Core model again. If it is not successful, then you should delete the "models" folder and train it again. The training steps are
described in [Building a Simple Bot][1].

**Running the server**

You can run a simple http server that handles requests using your models with

	python -m rasa_core.server -d examples/moodbot/models/dialogue -u examples/moodbot/models/nlu/current -o out.log
	
called from path/Lib/site-packages/ folder.

The different parameters are:

	-d, which is the path to the Rasa Core model.
	-u, which is the path to the Rasa NLU model.
	-o, which is the path to the log file.
	
**Starting a conversation**

You need to do a POST to the /conversation/<sender>/parse endpoint. 
<sender> is the conversation id (e.g. default if you just have one user, or the facebook user id or any other identifier).

	curl -i -XPOST http://localhost:5005/conversations/default/parse -d "{\"query\":\"hello there\"}" (on Windows)
	curl -XPOST http://localhost:5005/conversations/default/parse -d '{"query":"hello there"}' (on Linux/macOS)
	
The server will respond with either a particular next action that you should take or with an "action_listen" response. This
depends on the training of the bot and his domain. The following snippet represents a response from a restaurant search bot:

	{
	  "next_action": "utter_ask_howcanhelp",
	  "tracker": {
		"slots": {
		  "info": null,
		  "cuisine": null,
		  "people": null,
		  "matches": null,
		  "price": null,
		  "location": null
		},
		"sender_id": "default",
		"latest_message": {
		  ...
		}
	  }
	}

The next action that the user should take is "utter_ask_howcanhelp". 
After you finished running the mentioned action, you need to notify Rasa Core about that:
	
	curl -i -XPOST http://localhost:5005/conversations/default/continue -d \
    "{\"executed_action\": \"utter_ask_howcanhelp\", \"events\": []}" (on Windows)
	
	curl -XPOST http://localhost:5005/conversations/default/continue -d \
    '{"executed_action": "utter_ask_howcanhelp", "events": []}' (on Linux/macOS)
	
Here the API should respond with:

	{
	  "next_action":"action_listen",
	  "tracker": {
		"slots": {
		  "info": null,
		  "cuisine": null,
		  "people": null,
		  "matches": null,
		  "price": null,
		  "location": null
		},
		"sender_id": "default",
		"latest_message": {
		  ...
		}
	  }
	}
	
This response tells you to wait for the next user message. 
You should not call the continue endpoint after you received a response containing "action_listen" as the next action. 
Instead, wait for the next user message and call /conversations/default/parse again 
followed by subsequent calls to /conversations/default/continue until you get "action_listen" again.

----------

  [1]: https://core.rasa.ai/tutorial_basics.html#tutorial-basics
