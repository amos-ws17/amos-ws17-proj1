class Session:


    def __init__(self):
        self.current_dialogue_topic = None
        self.active_topics = []
        self.reset_flag = False

    def set_current_dialogue_topic(self, current_dialogue):
        self.current_dialogue_topic = current_dialogue

    def get_current_dialogue_topic(self):
        return self.current_dialogue_topic

    def add_active_topic(self, topic):
        self.active_topics.append(topic)

    def get_active_topics(self):
        return self.active_topics

    def set_reset_flag(self, value):
        self.reset_flag = value
