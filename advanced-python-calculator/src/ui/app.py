from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import uic
import sys

class CalculatorApp(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('src/ui/views/main_window.ui', self)
        self.init_ui()

    def init_ui(self):
        # Initialize UI components and connect signals
        pass

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = CalculatorApp()
    window.show()
    sys.exit(app.exec_())