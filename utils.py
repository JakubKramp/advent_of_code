def load_input(filename: str = 'input.txt') -> str:
    with open(filename, 'r') as f:
        input_data = f.read()
    return input_data
