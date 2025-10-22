from PyQt5.QtWidgets import (QMainWindow, QVBoxLayout, QHBoxLayout, QGridLayout, 
                          QWidget, QPushButton, QLineEdit, QLabel, QGraphicsDropShadowEffect,
                          QSizePolicy)
from PyQt5.QtCore import Qt, QPropertyAnimation, QEasingCurve, QSize
from PyQt5.QtGui import QColor, QFont, QIcon, QLinearGradient, QPalette, QBrush

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("NeoCalc X")
        self.setGeometry(100, 100, 400, 600)
        self.setStyleSheet("""
            QMainWindow {
                background-color: #121212;
            }
            QWidget {
                background-color: #121212;
                color: #FFFFFF;
            }
        """)
        self.initUI()

    def initUI(self):
        # Create central widget with dark theme
        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)
        
        # Main layout
        main_layout = QVBoxLayout(central_widget)
        main_layout.setSpacing(15)
        main_layout.setContentsMargins(20, 20, 20, 20)
        
        # Create display area with modern styling
        display_widget = QWidget()
        display_widget.setStyleSheet("""
            QWidget {
                background-color: #1E1E1E;
                border-radius: 15px;
                padding: 10px;
            }
        """)
        display_layout = QVBoxLayout(display_widget)
        
        # Expression display (shows current calculation)
        self.expression_display = QLabel("")
        self.expression_display.setAlignment(Qt.AlignRight)
        self.expression_display.setStyleSheet("""
            font-family: 'Segoe UI', Arial;
            font-size: 14px;
            color: #8E8E8E;
            padding: 5px;
        """)
        display_layout.addWidget(self.expression_display)
        
        # Main display
        self.display = QLineEdit("0")
        self.display.setAlignment(Qt.AlignRight)
        self.display.setReadOnly(True)
        self.display.setStyleSheet("""
            QLineEdit {
                border: none;
                background-color: transparent;
                font-family: 'Segoe UI', Arial;
                font-size: 36px;
                font-weight: bold;
                color: #FFFFFF;
                padding: 5px;
            }
        """)
        display_layout.addWidget(self.display)
        
        # Add shadow effect to display
        shadow = QGraphicsDropShadowEffect()
        shadow.setBlurRadius(15)
        shadow.setColor(QColor(0, 0, 0, 80))
        shadow.setOffset(0, 5)
        display_widget.setGraphicsEffect(shadow)
        
        main_layout.addWidget(display_widget)
        
        # Create button grid with modern styling
        button_widget = QWidget()
        button_widget.setStyleSheet("""
            QWidget {
                background-color: #1E1E1E;
                border-radius: 15px;
            }
        """)
        button_layout = QGridLayout(button_widget)
        button_layout.setSpacing(12)
        button_layout.setContentsMargins(15, 15, 15, 15)
        
        # Define button styles
        button_styles = {
            "number": """
                QPushButton {
                    background-color: #2D2D2D;
                    color: #FFFFFF;
                    font-family: 'Segoe UI', Arial;
                    font-size: 18px;
                    font-weight: bold;
                    border-radius: 20px;
                    padding: 15px;
                    min-height: 50px;
                }
                QPushButton:hover {
                    background-color: #3D3D3D;
                }
                QPushButton:pressed {
                    background-color: #4D4D4D;
                }
            """,
            "operator": """
                QPushButton {
                    background-color: #FF8C00;
                    color: #FFFFFF;
                    font-family: 'Segoe UI', Arial;
                    font-size: 18px;
                    font-weight: bold;
                    border-radius: 20px;
                    padding: 15px;
                    min-height: 50px;
                }
                QPushButton:hover {
                    background-color: #FFA500;
                }
                QPushButton:pressed {
                    background-color: #FFB700;
                }
            """,
            "function": """
                QPushButton {
                    background-color: #1E1E1E;
                    color: #FF8C00;
                    font-family: 'Segoe UI', Arial;
                    font-size: 18px;
                    font-weight: bold;
                    border-radius: 20px;
                    border: 2px solid #FF8C00;
                    padding: 15px;
                    min-height: 50px;
                }
                QPushButton:hover {
                    background-color: #2D2D2D;
                }
                QPushButton:pressed {
                    background-color: #3D3D3D;
                }
            """,
            "equals": """
                QPushButton {
                    background-color: #4CAF50;
                    color: #FFFFFF;
                    font-family: 'Segoe UI', Arial;
                    font-size: 18px;
                    font-weight: bold;
                    border-radius: 20px;
                    padding: 15px;
                    min-height: 50px;
                }
                QPushButton:hover {
                    background-color: #5CBF60;
                }
                QPushButton:pressed {
                    background-color: #6CCF70;
                }
            """
        }
        
        # Define buttons with their positions and styles
        buttons = [
            ('C', 0, 0, 1, 1, self.clear_display, "function"),
            ('⌫', 0, 1, 1, 1, self.backspace, "function"),
            ('%', 0, 2, 1, 1, lambda: self.add_to_display('%'), "function"),
            ('÷', 0, 3, 1, 1, lambda: self.add_to_display('/'), "operator"),
            
            ('7', 1, 0, 1, 1, lambda: self.add_to_display('7'), "number"),
            ('8', 1, 1, 1, 1, lambda: self.add_to_display('8'), "number"),
            ('9', 1, 2, 1, 1, lambda: self.add_to_display('9'), "number"),
            ('×', 1, 3, 1, 1, lambda: self.add_to_display('*'), "operator"),
            
            ('4', 2, 0, 1, 1, lambda: self.add_to_display('4'), "number"),
            ('5', 2, 1, 1, 1, lambda: self.add_to_display('5'), "number"),
            ('6', 2, 2, 1, 1, lambda: self.add_to_display('6'), "number"),
            ('-', 2, 3, 1, 1, lambda: self.add_to_display('-'), "operator"),
            
            ('1', 3, 0, 1, 1, lambda: self.add_to_display('1'), "number"),
            ('2', 3, 1, 1, 1, lambda: self.add_to_display('2'), "number"),
            ('3', 3, 2, 1, 1, lambda: self.add_to_display('3'), "number"),
            ('+', 3, 3, 1, 1, lambda: self.add_to_display('+'), "operator"),
            
            ('±', 4, 0, 1, 1, self.negate, "number"),
            ('0', 4, 1, 1, 1, lambda: self.add_to_display('0'), "number"),
            ('.', 4, 2, 1, 1, lambda: self.add_to_display('.'), "number"),
            ('=', 4, 3, 1, 1, self.calculate_result, "equals"),
        ]
        
        # Add buttons to grid
        for (text, row, col, rowspan, colspan, handler, style_type) in buttons:
            button = QPushButton(text)
            button.setStyleSheet(button_styles[style_type])
            button.clicked.connect(handler)
            button_layout.addWidget(button, row, col, rowspan, colspan)
            
            # Add shadow effect to buttons
            shadow = QGraphicsDropShadowEffect()
            shadow.setBlurRadius(10)
            shadow.setColor(QColor(0, 0, 0, 50))
            shadow.setOffset(0, 3)
            button.setGraphicsEffect(shadow)
        
        # Add button widget to main layout
        main_layout.addWidget(button_widget)
        
        # Add advanced functions row
        advanced_widget = QWidget()
        advanced_widget.setStyleSheet("""
            QWidget {
                background-color: #1E1E1E;
                border-radius: 15px;
            }
        """)
        advanced_layout = QHBoxLayout(advanced_widget)
        advanced_layout.setSpacing(10)
        
        advanced_buttons = [
            ('sin', lambda: self.add_function('sin')),
            ('cos', lambda: self.add_function('cos')),
            ('tan', lambda: self.add_function('tan')),
            ('√', lambda: self.add_function('sqrt')),
            ('π', lambda: self.add_to_display('3.14159'))
        ]
        
        for (text, handler) in advanced_buttons:
            button = QPushButton(text)
            button.setStyleSheet(button_styles["function"])
            button.clicked.connect(handler)
            advanced_layout.addWidget(button)
        
        main_layout.addWidget(advanced_widget)

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
