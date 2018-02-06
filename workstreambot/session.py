class Session:
    current_dialogue_topic = None
    all_topics = []
    reset_flag = False

    def set_current_dialogue_topic(self, current_dialogue):
        self.current_dialogue_topic = current_dialogue

    def get_current_dialogue_topic(self):
        return self.current_dialogue_topic

    def add_new_topic(self, new_topic):
        self.all_topics.append(new_topic)

    def set_reset_flag(self, value):
        self.reset_flag = value