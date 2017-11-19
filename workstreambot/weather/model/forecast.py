class Forecast(object):
    # init method
    def __init__(self, forecast_data):
        self._forecast_data = forecast_data
    # parse the description of the forecast
    def text(self):
        return self._forecast_data['text']
    # parse the date to which the forecast applies
    def date(self):
        return self._forecast_data['date']
    # the forecasted high temperature for this day
    def high(self):
        return self._forecast_data['high']
    # the forecasted low temperature for this day
    def low(self):
        return self._forecast_data['low']
