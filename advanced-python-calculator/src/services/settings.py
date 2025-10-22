class Settings:
    def __init__(self):
        self.theme = "default"
        self.language = "en"
        self.history_enabled = True

    def set_theme(self, theme):
        self.theme = theme

    def get_theme(self):
        return self.theme

    def set_language(self, language):
        self.language = language

    def get_language(self):
        return self.language

    def enable_history(self):
        self.history_enabled = True

    def disable_history(self):
        self.history_enabled = False

    def is_history_enabled(self):
        return self.history_enabled

    def reset_to_defaults(self):
        self.theme = "default"
        self.language = "en"
        self.history_enabled = True