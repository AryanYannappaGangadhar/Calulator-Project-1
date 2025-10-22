import unittest
from src.calculator.parser import Parser

class TestParser(unittest.TestCase):

    def setUp(self):
        self.parser = Parser()

    def test_simple_expression(self):
        expression = "3 + 5"
        expected_output = [('NUMBER', 3), ('PLUS', '+'), ('NUMBER', 5)]
        self.assertEqual(self.parser.parse(expression), expected_output)

    def test_complex_expression(self):
        expression = "10 - 2 * 3"
        expected_output = [('NUMBER', 10), ('MINUS', '-'), ('NUMBER', 2), ('TIMES', '*'), ('NUMBER', 3)]
        self.assertEqual(self.parser.parse(expression), expected_output)

    def test_parentheses(self):
        expression = "(1 + 2) * 3"
        expected_output = [('LPAREN', '('), ('NUMBER', 1), ('PLUS', '+'), ('NUMBER', 2), ('RPAREN', ')'), ('TIMES', '*'), ('NUMBER', 3)]
        self.assertEqual(self.parser.parse(expression), expected_output)

    def test_invalid_expression(self):
        expression = "3 + * 5"
        with self.assertRaises(SyntaxError):
            self.parser.parse(expression)

if __name__ == '__main__':
    unittest.main()