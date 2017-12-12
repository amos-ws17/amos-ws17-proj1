from __future__ import unicode_literals

def train_nlu():
    from rasa_nlu.converters import load_data
    from rasa_nlu.config import RasaNLUConfig
    from rasa_nlu.model import Trainer

    training_data = load_data('data/train_full.json')
    trainer = Trainer(RasaNLUConfig("nlu_model_config.json"))
    trainer.train(training_data)
    model_directory = trainer.persist('models/nlu/', fixed_model_name="current")

    return model_directory

def train_dialogue():
    from rasa_core.agent import Agent
    from rasa_core.policies.keras_policy import KerasPolicy
    from rasa_core.policies.memoization import MemoizationPolicy

    domain_file="domain.yml"
    model_path="models/dialogue"
    stories_file="data/stories.md"

    agent = Agent(domain_file, policies=[MemoizationPolicy(), KerasPolicy()])
    agent.train(stories_file)
    agent.persist(model_path)

    return agent

if __name__ == '__main__':
    train_nlu()
    train_dialogue()