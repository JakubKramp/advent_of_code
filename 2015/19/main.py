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

def get_steps():
    steps = 0
    molecule = target_string
    while len(molecule)>1:
        for rule in rules:
            for key, value in rule.items():
                if count := molecule.count(value):
                    molecule = molecule.replace(value, key)
                    steps += count
    return steps

print_answer(len(combinations), get_steps())
