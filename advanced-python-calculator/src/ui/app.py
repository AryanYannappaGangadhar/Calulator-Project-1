from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import uic
import sys
from ui.views.main_window import MainWindow

class CalculatorApp(MainWindow):
    def __init__(self):
        super().__init__()
        # The MainWindow class already sets up the UI

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = CalculatorApp()
    window.show()
    sys.exit(app.exec_())
