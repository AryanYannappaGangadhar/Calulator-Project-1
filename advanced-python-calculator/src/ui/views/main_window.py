
from PyQt5.QtWidgets import (QMainWindow, QVBoxLayout, QHBoxLayout, QGridLayout, 
                          QWidget, QPushButton, QLineEdit, QLabel, QGraphicsDropShadowEffect,
                          QSizePolicy, QGraphicsOpacityEffect, QSplashScreen)
from PyQt5.QtCore import Qt, QPropertyAnimation, QEasingCurve, QSize, QTimer, QPoint, QRect, QSequentialAnimationGroup, QParallelAnimationGroup
from PyQt5.QtGui import QColor, QFont, QIcon, QLinearGradient, QPalette, QBrush, QPixmap, QPainter, QRadialGradient
import random
import math

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
        
        # Show splash screen before initializing UI
        self.show_splash_screen()
        
        # Animation properties
        self.button_animations = {}
        self.current_animation = None
        self.particles = []
        
        # Initialize UI after splash screen
        QTimer.singleShot(2500, self.initUI)
        
    def show_splash_screen(self):
        # Create a cool splash screen
        splash_pixmap = QPixmap(400, 600)
        splash_pixmap.fill(Qt.transparent)
        
        painter = QPainter(splash_pixmap)
        painter.setRenderHint(QPainter.Antialiasing)
        
        # Create gradient background
        gradient = QRadialGradient(200, 300, 300)
        gradient.setColorAt(0, QColor(80, 20, 120))
        gradient.setColorAt(0.5, QColor(40, 10, 80))
        gradient.setColorAt(1, QColor(20, 5, 40))
        
        painter.setBrush(gradient)
        painter.setPen(Qt.NoPen)
        painter.drawRect(0, 0, 400, 600)
        
        # Draw app name
        painter.setFont(QFont("Segoe UI", 36, QFont.Bold))
        painter.setPen(QColor(255, 140, 0))
        painter.drawText(QRect(0, 200, 400, 100), Qt.AlignCenter, "NeoCalc X")
        
        # Draw tagline
        painter.setFont(QFont("Segoe UI", 14))
        painter.setPen(QColor(200, 200, 200))
        painter.drawText(QRect(0, 300, 400, 50), Qt.AlignCenter, "Next-Gen Calculator")
        
        # Draw some decorative elements
        painter.setPen(Qt.NoPen)
        for i in range(20):
            x = random.randint(0, 400)
            y = random.randint(0, 600)
            size = random.randint(5, 20)
            opacity = random.randint(50, 200)
            painter.setBrush(QColor(255, 140, 0, opacity))
            painter.drawEllipse(x, y, size, size)
        
        painter.end()
        
        # Create and show splash screen
        self.splash = QSplashScreen(splash_pixmap, Qt.WindowStaysOnTopHint)
        self.splash.show()
        
        # Create animation for splash screen elements
        def animate_splash():
            for i in range(10):
                x = random.randint(0, 400)
                y = random.randint(0, 600)
                size = random.randint(5, 20)
                
                pixmap = QPixmap(splash_pixmap)
                painter = QPainter(pixmap)
                painter.setRenderHint(QPainter.Antialiasing)
                
                painter.setPen(Qt.NoPen)
                painter.setBrush(QColor(255, 255, 255, 150))
                painter.drawEllipse(x, y, size, size)
                
                painter.end()
                
                self.splash.setPixmap(pixmap)
                QTimer.singleShot(i * 200, lambda p=pixmap: self.splash.setPixmap(p))
        
        # Start splash animation
        QTimer.singleShot(100, animate_splash)
        
        # Close splash after delay
        QTimer.singleShot(2500, self.splash.close)

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
        
        # Add buttons to grid with animations
        for (text, row, col, rowspan, colspan, handler, style_type) in buttons:
            button = QPushButton(text)
            button.setStyleSheet(button_styles[style_type])
            
            # Create a custom click handler that includes animation
            def create_animated_handler(original_handler, btn):
                def animated_handler():
                    # Play button press animation
                    self.animate_button_press(btn)
                    # Call the original handler
                    original_handler()
                return animated_handler
            
            # Connect the animated handler
            button.clicked.connect(create_animated_handler(handler, button))
            button_layout.addWidget(button, row, col, rowspan, colspan)
            
            # Add shadow effect to buttons
            shadow = QGraphicsDropShadowEffect()
            shadow.setBlurRadius(10)
            shadow.setColor(QColor(0, 0, 0, 50))
            shadow.setOffset(0, 3)
            button.setGraphicsEffect(shadow)
            
            # Store button for later animations
            self.button_animations[text] = button
            
            # Add entrance animation for each button with delay based on position
            delay = (row * 4 + col) * 50  # Staggered delay
            QTimer.singleShot(2500 + delay, lambda b=button: self.animate_button_entrance(b))
        
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
        if current_text == "0" and value not in ['.', '+', '-', '*', '/']:
            self.display.setText(value)
        else:
            new_text = current_text + value
            self.display.setText(new_text)
        
        # Update expression display
        self.expression_display.setText(self.display.text())

    def add_function(self, func):
        function_map = {
            'sin': 'sin(',
            'cos': 'cos(',
            'tan': 'tan(',
            'sqrt': 'sqrt('
        }
        current_text = self.display.text()
        if current_text == "0":
            self.display.setText(function_map.get(func, func + '('))
        else:
            self.display.setText(current_text + function_map.get(func, func + '('))
        
        # Update expression display
        self.expression_display.setText(self.display.text())

    def clear_display(self):
        self.display.setText("0")
        self.expression_display.setText("")

    def backspace(self):
        current_text = self.display.text()
        if len(current_text) > 1:
            self.display.setText(current_text[:-1])
        else:
            self.display.setText("0")
        
        # Update expression display
        self.expression_display.setText(self.display.text())

    def negate(self):
        current_text = self.display.text()
        if current_text != "0":
            if current_text.startswith('-'):
                self.display.setText(current_text[1:])
            else:
                self.display.setText('-' + current_text)
            
            # Update expression display
            self.expression_display.setText(self.display.text())

    def calculate_result(self):
        try:
            expression = self.display.text()
            # Store the expression for history
            self.expression_display.setText(expression + " =")
            
            # Calculate the result
            # For safety, we'll use eval with some basic validation
            # In a production app, you'd want a more secure expression evaluator
            if any(op in expression for op in ['+', '-', '*', '/', '(', ')']):
                result = eval(expression)
                
                # Format the result
                if isinstance(result, float):
                    # Limit decimal places for cleaner display
                    if result.is_integer():
                        result = int(result)
                    else:
                        result = round(result, 8)
                
                # Update display with result
                self.display.setText(str(result))
            else:
                # If it's just a number, keep it as is
                pass
                
        except Exception as e:
            self.display.setText("Error")
            self.expression_display.setText("Invalid expression")
            print(f"Calculation error: {e}")

    def animate_button_entrance(self, button):
        """Create an entrance animation for buttons"""
        # Save original position and size
        original_geometry = button.geometry()
        
        # Create opacity effect
        opacity_effect = QGraphicsOpacityEffect(button)
        button.setGraphicsEffect(opacity_effect)
        opacity_effect.setOpacity(0)
        
        # Create opacity animation
        opacity_anim = QPropertyAnimation(opacity_effect, b"opacity")
        opacity_anim.setDuration(300)
        opacity_anim.setStartValue(0)
        opacity_anim.setEndValue(1)
        opacity_anim.setEasingCurve(QEasingCurve.OutCubic)
        
        # Create position animation
        pos_anim = QPropertyAnimation(button, b"geometry")
        pos_anim.setDuration(300)
        
        # Start from a random direction
        direction = random.choice(["top", "bottom", "left", "right"])
        start_geometry = QRect(original_geometry)
        
        if direction == "top":
            start_geometry.moveTop(original_geometry.top() - 50)
        elif direction == "bottom":
            start_geometry.moveTop(original_geometry.top() + 50)
        elif direction == "left":
            start_geometry.moveLeft(original_geometry.left() - 50)
        elif direction == "right":
            start_geometry.moveLeft(original_geometry.left() + 50)
        
        pos_anim.setStartValue(start_geometry)
        pos_anim.setEndValue(original_geometry)
        pos_anim.setEasingCurve(QEasingCurve.OutBack)
        
        # Create animation group
        anim_group = QParallelAnimationGroup()
        anim_group.addAnimation(opacity_anim)
        anim_group.addAnimation(pos_anim)
        anim_group.start()
    
    def animate_button_press(self, button):
        """Create a press animation for buttons"""
        # Create scale animation
        anim = QPropertyAnimation(button, b"geometry")
        anim.setDuration(100)
        
        # Get current geometry
        current_geometry = button.geometry()
        
        # Create a slightly smaller geometry for the "pressed" state
        pressed_geometry = QRect(current_geometry)
        pressed_geometry.setWidth(int(current_geometry.width() * 0.95))
        pressed_geometry.setHeight(int(current_geometry.height() * 0.95))
        pressed_geometry.moveCenter(current_geometry.center())
        
        # Set up the animation
        anim.setStartValue(current_geometry)
        anim.setEndValue(pressed_geometry)
        anim.setEasingCurve(QEasingCurve.OutQuad)
        
        # Create the release animation
        release_anim = QPropertyAnimation(button, b"geometry")
        release_anim.setDuration(200)
        release_anim.setStartValue(pressed_geometry)
        release_anim.setEndValue(current_geometry)
        release_anim.setEasingCurve(QEasingCurve.OutElastic)
        
        # Create sequential animation group
        anim_group = QSequentialAnimationGroup()
        anim_group.addAnimation(anim)
        anim_group.addAnimation(release_anim)
        anim_group.start()
    
    def animate_calculation(self):
        """Create a calculation animation effect"""
        # Create a particle effect around the display
        for i in range(20):
            # Create a particle label
            particle = QLabel(self)
            particle.setFixedSize(10, 10)
            
            # Random color
            color = random.choice(["#FF8C00", "#4CAF50", "#2196F3", "#9C27B0"])
            
            # Set particle style
            particle.setStyleSheet(f"""
                background-color: {color};
                border-radius: 5px;
            """)
            
            # Random position around the display
            display_rect = self.display.geometry()
            x = display_rect.x() + random.randint(0, display_rect.width())
            y = display_rect.y() + display_rect.height() + random.randint(-10, 10)
            
            particle.move(x, y)
            particle.show()
            
            # Create animation
            anim = QPropertyAnimation(particle, b"pos")
            anim.setDuration(random.randint(500, 1500))
            anim.setStartValue(QPoint(x, y))
            
            # Random end position
            end_x = x + random.randint(-100, 100)
            end_y = y + random.randint(-100, 100)
            anim.setEndValue(QPoint(end_x, end_y))
            
            # Random curve
            anim.setEasingCurve(random.choice([
                QEasingCurve.OutQuad,
                QEasingCurve.OutCubic,
                QEasingCurve.OutQuart
            ]))
            
            # Create opacity animation
            opacity_effect = QGraphicsOpacityEffect(particle)
            particle.setGraphicsEffect(opacity_effect)
            
            opacity_anim = QPropertyAnimation(opacity_effect, b"opacity")
            opacity_anim.setDuration(random.randint(500, 1500))
            opacity_anim.setStartValue(1.0)
            opacity_anim.setEndValue(0.0)
            
            # Group animations
            group = QParallelAnimationGroup()
            group.addAnimation(anim)
            group.addAnimation(opacity_anim)
            
            # Clean up when done
            group.finished.connect(lambda p=particle: p.deleteLater())
            
            group.start()
    
    def calculate_result(self):
        try:
            expression = self.display.text()
            # Store the expression for history
            self.expression_display.setText(expression + " =")
            
            # Calculate the result
            # For safety, we'll use eval with some basic validation
            # In a production app, you'd want a more secure expression evaluator
            if any(op in expression for op in ['+', '-', '*', '/', '(', ')']):
                result = eval(expression)
                
                # Format the result
                if isinstance(result, float):
                    # Limit decimal places for cleaner display
                    if result.is_integer():
                        result = int(result)
                    else:
                        result = round(result, 8)
                
                # Play calculation animation
                self.animate_calculation()
                
                # Update display with result
                self.display.setText(str(result))
            else:
                # If it's just a number, keep it as is
                pass
                
        except Exception as e:
            self.display.setText("Error")
            self.expression_display.setText("Invalid expression")
            print(f"Calculation error: {e}")
    
    def closeEvent(self, event):
        event.accept()  # Accept the event to close the window
