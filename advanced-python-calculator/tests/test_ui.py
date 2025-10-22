import unittest
from src.ui.app import CalculatorApp

class TestCalculatorUI(unittest.TestCase):

    def setUp(self):
        self.app = CalculatorApp()

    def test_initialization(self):
        self.assertIsNotNone(self.app)
        self.assertTrue(self.app.is_running)

    def test_button_click(self):
        button = self.app.ui.widgets.get_button('1')
        button.click()
        self.assertEqual(self.app.ui.display.text(), '1')

    def test_calculation(self):
        self.app.ui.widgets.get_button('1').click()
        self.app.ui.widgets.get_button('+').click()
        self.app.ui.widgets.get_button('2').click()
        self.app.ui.widgets.get_button('=').click()
        self.assertEqual(self.app.ui.display.text(), '3')

    def test_clear_functionality(self):
        self.app.ui.widgets.get_button('1').click()
        self.app.ui.widgets.get_button('C').click()
        self.assertEqual(self.app.ui.display.text(), '')

if __name__ == '__main__':
    unittest.main()