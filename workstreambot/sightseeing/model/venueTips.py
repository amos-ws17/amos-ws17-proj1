class VenueTips(object):
    # init method
    def __init__(self, tips_data):
        self._tips_data = tips_data

    # Parse the id of the tip
    def getTipId(self):
        return self._tips_data['id']

    # Parse the text of the tip
    def getTipText(self):
        return self._tips_data['text']

    # Parse the user of the tip
    def getTipUser(self):
        if 'firstName' in self._tips_data['user']:
            return self._tips_data['user']['firstName']
        return "Anonymous User"
