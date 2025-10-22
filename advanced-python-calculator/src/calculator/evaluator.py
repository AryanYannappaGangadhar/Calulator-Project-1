class Evaluator:
    def __init__(self):
        pass

    def evaluate(self, expression):
        try:
            # Here we can use eval for simplicity, but in a real-world scenario,
            # we should use a safer method to evaluate expressions.
            result = eval(expression)
            return result
        except Exception as e:
            return f"Error evaluating expression: {e}"