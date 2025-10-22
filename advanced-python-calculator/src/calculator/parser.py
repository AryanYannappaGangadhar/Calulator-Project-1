class Parser:
    def __init__(self):
        pass

    def parse(self, user_input):
        # Basic parsing logic to convert user input into a format suitable for evaluation
        tokens = self.tokenize(user_input)
        return tokens

    def tokenize(self, user_input):
        # Tokenization logic to split the input into manageable parts
        tokens = []
        current_number = ''
        for char in user_input:
            if char.isdigit() or char == '.':
                current_number += char
            else:
                if current_number:
                    tokens.append(float(current_number))
                    current_number = ''
                if char in '+-*/()':
                    tokens.append(char)
        if current_number:
            tokens.append(float(current_number))
        return tokens