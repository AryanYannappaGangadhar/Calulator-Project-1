class History:
    def __init__(self):
        self.history = []

    def add_entry(self, expression, result):
        self.history.append({'expression': expression, 'result': result})

    def get_history(self):
        return self.history

    def clear_history(self):
        self.history.clear()