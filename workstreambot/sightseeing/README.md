## Demo setup

'''
python -m rasa_nlu.train -c nlu_model_config.json --fixed_model_name current
'''

'''
python -m rasa_core.train -s data/stories.md -d domain.yml -o models/dialogue --epochs 300
'''

'''
python -m rasa_core.run -d project/dialogue -u project/nlu/current
'''


# Demo chat 1
hello

can you recommend me a monument in berlin?

i don't like it

nice i like it

what's its opening time?

thanks



# Demo chat 2
hi

i need some recommendations for outdoor places in berlin

cheap

nice

when is it opened?

thank you
