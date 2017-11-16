----------

How to access Rasa Core and Rasa NLU Http servers on the AWS Server
-------------

From Sprint 4 on, the team has an AWS server, where the bot, that the team is developing is deployed and can be accessed.

**Rasa NLU http server access**

In order to make requests to the Rasa NLU server you can either use the command prompt of you computer or
directly the web browser that you have. The following two commands represent a simple "hello there" query to the Rasa NLU server.

	curl -XPOST http://ec2-34-214-151-224.us-west-2.compute.amazonaws.com:5000/parse -d '{"q":"hello there"}' (from the console)
	http://ec2-34-214-151-224.us-west-2.compute.amazonaws.com:5000/parse?q=hello%20there (from the web browser)

The response of the server should look like the following

	{"entities": [], "intent": {"confidence": 1.0, "name": "greet"}, "text": "hello there"}

**Rasa Core http server access**

In order to make requests to the Rasa Core server you can either use the command prompt of you computer or
directly the web browser that you have. The following two commands represent a simple "hello there" query to the Rasa Core server.

	curl -XPOST http://ec2-34-214-151-224.us-west-2.compute.amazonaws.com:5005/conversations/default/parse -d '{"query":"hello there"}' (from the console)
	http://ec2-34-214-151-224.us-west-2.compute.amazonaws.com:5005/conversations/default/parse?q=hello%20there (from the web browser)

The response of the server should look like the following (depends on the bot)

	{"next_action": "utter_goodbye", "tracker": {"sender_id": "default", "slots": {}, 
	"latest_message": {"intent": {"name": "mood_deny", "confidence": 0.199249624820521}, 
	"entities": [], "intent_ranking": [{"name": "mood_deny", "confidence": 0.199249624820521}, 
	{"name": "mood_affirm", "confidence": 0.19564884489623477}, {"name": "goodbye", "confidence": 0.18983993016534373}, 
	{"name": "greet", "confidence": 0.1798304981646691}, {"name": "mood_great", "confidence": 0.13731384329498864}, 
	{"name": "mood_unhappy", "confidence": 0.09811725865824238}], "text": "hello there"}}}

	
If you encounter any problems you can ask Veselin or Daniel.

