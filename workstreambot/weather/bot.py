from __future__ import unicode_literals
from rasa_nlu.config import RasaNLUConfig
from rasa_core.agent import Agent

def train_nlu():
    from rasa_nlu.converters import load_data
    from rasa_nlu.model import Trainer

    training_data = load_data('data/train_full.json')
    trainer = Trainer(RasaNLUConfig("nlu_model_config.json"))
    trainer.train(training_data)
    model_directory = trainer.persist('models/nlu/', fixed_model_name="current")

    return model_directory

def train_dialogue(topic):
    from rasa_core.policies.keras_policy import KerasPolicy
    from rasa_core.policies.memoization import MemoizationPolicy

    domain_file = topic + "domain.yml"
    model_path = topic + "models/dialogue"
    stories_file = topic + "data/stories.md"

    agent = Agent(domain_file, policies=[MemoizationPolicy(), KerasPolicy()])
    agent.train(stories_file)
    agent.persist(model_path)

    return model_path

def load_interpreter(model_directory):
    from rasa_nlu.model import Metadata, Interpreter

    # where `model_directory points to the folder the model is persisted in
    interpreter = Interpreter.load(model_directory, RasaNLUConfig("nlu_model_config.json"))

    return interpreter

def load_agent(model_path):
    return Agent.load(model_path)

if __name__ == '__main__':
    #train nlu
    #model_path = train_nlu()
    #train dialogue
    topic = ""
    #dialogue_path = train_dialogue(topic)

    model_path = "models/nlu/default/current"
    dialogue_path = topic + "models/dialogue"

    #parse user input
    interpreter = load_interpreter(model_path)
    nlu_jsonResponse = interpreter.parse("What will the weather be in Berlin?") # should return the same dict as the HTTP api would (without emulation).

    entities = []

    if len(nlu_jsonResponse['entities']) > 0:

        for e in nlu_jsonResponse['entities']:
            entity = e['entity'] + "=" + e['value']
            entities.append(entity)

    #handle user input
    agent = load_agent(dialogue_path)
    print agent.handle_message('_' + nlu_jsonResponse['intent']['name'] + '[' + ','.join(map(str,entities)) + ']')
