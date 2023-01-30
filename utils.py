def load_input(filename: str = 'input.txt') -> str:
    with open(filename, 'r') as f:
        input_data = f.read()
    return input_data


def print_answer(first_part: int, second_part: int = 0):
    answer = f'---PART ONE---\n{first_part}'
    if second_part:
        answer += f'\n---PART TWO---\n{second_part}'
    print(answer)
