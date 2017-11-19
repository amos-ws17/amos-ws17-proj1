class Condition(object):
    # init method
    def __init__(self, condition_data):
        self._condition_data = condition_data
    # parse the description of the condition
    def text(self):
        return self._condition_data['text']
    # parse the current date and time
    def date(self):
        return self._condition_data['date']
    # parse the condition code for this forecast
    def code(self):
        return self._condition_data['code']
    # parse the current temperature
    def temp(self):
        return self._condition_data['temp']
