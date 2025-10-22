from PyQt5.QtWidgets import QMainWindow, QVBoxLayout, QWidget, QPushButton, QLineEdit, QLabel
from PyQt5.QtCore import Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Advanced Python Calculator")
        self.setGeometry(100, 100, 400, 600)
        self.initUI()

    def initUI(self):
        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)

        layout = QVBoxLayout(central_widget)

        self.display = QLineEdit(self)
        self.display.setAlignment(Qt.AlignRight)
        self.display.setReadOnly(True)
        layout.addWidget(self.display)

        self.result_label = QLabel("Result:", self)
        layout.addWidget(self.result_label)

        button_layout = QVBoxLayout()

        # Example buttons
        buttons = [
            ('7', self.add_to_display),
            ('8', self.add_to_display),
            ('9', self.add_to_display),
            ('/', self.add_to_display),
            ('4', self.add_to_display),
            ('5', self.add_to_display),
            ('6', self.add_to_display),
            ('*', self.add_to_display),
            ('1', self.add_to_display),
            ('2', self.add_to_display),
            ('3', self.add_to_display),
            ('-', self.add_to_display),
            ('0', self.add_to_display),
            ('C', self.clear_display),
            ('=', self.calculate_result),
            ('+', self.add_to_display),
        ]

        for (text, handler) in buttons:
            button = QPushButton(text, self)
            button.clicked.connect(lambda checked, t=text: handler(t))
            button_layout.addWidget(button)

        layout.addLayout(button_layout)

    def add_to_display(self, value):
        current_text = self.display.text()
        new_text = current_text + value
        self.display.setText(new_text)

    def clear_display(self):
        self.display.clear()

    def calculate_result(self):
        try:
            expression = self.display.text()
            # Here you would call the evaluator to compute the result
            # For now, we will just display the expression
            self.result_label.setText(f"Result: {expression}")
        except Exception as e:
            self.result_label.setText("Error")

    def closeEvent(self, event):
        event.accept()  # Accept the event to close the window