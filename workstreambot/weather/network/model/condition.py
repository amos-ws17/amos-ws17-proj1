class Condition(object):
    # init method
    def __init__(self, condition_data):
        self._condition_data = condition_data

    # parse the description of the condition
    def getConditionDescription(self):
        return self._condition_data['text']

    # parse the current date and time
    def getLastUpdatedConditionDate(self):
        return self._condition_data['date']

    # parse the current temperature
    def getConditionCurrentTemperature(self):
        return self._condition_data['temp']
