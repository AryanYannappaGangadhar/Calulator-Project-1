from PyQt5.QtWidgets import QApplication
from ui.app import App

def main():
    import sys
    app = QApplication(sys.argv)
    calculator_app = App()
    calculator_app.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()