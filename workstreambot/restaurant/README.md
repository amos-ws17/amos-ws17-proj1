# Demo setup

```
python -m rasa_nlu.train -c nlu_model_config.json --fixed_model_name current
```

```
python -m rasa_core.train -s data/stories.md -d domain.yml -o project/dialogue --epochs 100
```

```
python -m rasa_core.run -d project/dialogue -u project/nlu/current
```

# Demo dialogue
The bot welcomes you after greeting him and asks you for a city where you would like to find a restaurant

    You: Hey  
    Bot: Hey there!  
    Bot: In which city would you like to find a restaurant?

After you give him an answer, it will ask you about the type of cuisine and the price range

    You: In Berlin
    Bot: What kind of cuisine would you like and in which price range should it be?
         1: cheap <cheap>
         2: expensive <expensive>
    You: I would like to try some cheap mexican restaurant
    Bot: I'm on it
    Bot: I'm searching 
    Bot: <suggestion>

You can affirm the suggestion

    You: I like it  
    Bot: It was a pleasure for me to help you 
    Bot: Bye-bye
