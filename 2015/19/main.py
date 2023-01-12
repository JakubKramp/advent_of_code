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

def get_combinations():
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
    return combinations
combinations = get_combinations()
combinations.remove(target_string)

def reverse_molecule(target_string):
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
            replaced = mutable.replace(value, key, 1)
            product = immutable+replaced
            molecules.add(product)
    return molecules

print_answer(len(combinations))

molecules = set()
i = 0
while 'e' not in molecules:
    reverse_molecule()