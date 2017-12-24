class Session:
    dialogue_models = None
    current_dialogue_topic = None

    def __init__(self, agents):
        self.dialogue_models = agents

    def set_dialogue_models(self, agents):
        self.dialogue_models = agents

    def get_dialogue_models(self):
        return self.dialogue_models

    def set_current_dialogue_topic(self, current_dialogue):
        self.current_dialogue_topic = current_dialogue

    def get_current_dialogue_topic(self):
        return self.current_dialogue_topic
