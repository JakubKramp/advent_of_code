"""

"""

from utils import load_input, print_answer

replacements, target_string = load_input().split('\n\n')

def create_rules():
    rules = []
    r = []
    for replacement in replacements.split('\n'):
        key, value = replacement.split('=>')
        rules.append({key.strip(): value.strip()})
        r.append(key.strip())
    return rules
rules = create_rules()

def get_values():
    values = []
    for replacement in replacements.split('\n'):
        key, value = replacement.split('=>')
        values.append(value)
    return values

def get_combinations(target_string):
    combinations = set()
    for rule in rules:
        key = list(rule.keys())[0]
        value = list(rule.values())[0]
        occurrences = target_string.count(key)
        indices = [0]
        index = 0
        for i in range(occurrences):
            index = target_string.find(key, index) + 1
            if index:
                indices.append(index)
        for ind in indices:
            mutable, immutable = target_string[ind:], target_string[:ind]
            replaced = mutable.replace(key, value, 1)
            product = immutable+replaced
            combinations.add(product)
    combinations.remove(target_string)
    return combinations
combinations = get_combinations(target_string)


print_answer(len(combinations))

values = get_values()
def get_steps():
    strings = ['e']
    molecules = set()
    for i in range(2):
        for string in strings:
            molecules = get_combinations(string)
        strings = list(molecules)
        if target_string in molecules:
            return i + 1
    print(strings)
    return 'siema'


print(get_steps())


