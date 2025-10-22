class CustomButton(QtWidgets.QPushButton):
    def __init__(self, label, *args, **kwargs):
        super().__init__(label, *args, **kwargs)
        self.setStyleSheet("background-color: #4CAF50; color: white; font-size: 18px; border-radius: 5px;")
        self.setFixedSize(100, 50)

class DisplayField(QtWidgets.QLineEdit):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setStyleSheet("background-color: #f0f0f0; font-size: 24px; padding: 10px; border: 1px solid #ccc;")
        self.setReadOnly(True)
        self.setFixedHeight(50)

class HistoryListWidget(QtWidgets.QListWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setStyleSheet("background-color: #ffffff; font-size: 16px; border: 1px solid #ccc;")
        self.setFixedHeight(200)

class CalculatorWidget(QtWidgets.QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.layout = QtWidgets.QVBoxLayout(self)
        self.display = DisplayField()
        self.history = HistoryListWidget()
        self.layout.addWidget(self.display)
        self.layout.addWidget(self.history)
        self.setLayout(self.layout)