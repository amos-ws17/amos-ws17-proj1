class Session:
    current_dialogue_topic = None

    def set_current_dialogue_topic(self, current_dialogue):
        self.current_dialogue_topic = current_dialogue

    def get_current_dialogue_topic(self):
        return self.current_dialogue_topic
