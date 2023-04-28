"""
--- Day 7: Some Assembly Required ---
This year, Santa brought little Bobby Tables a set of wires and bitwise logic gates! Unfortunately, little Bobby is a little under the recommended age range, and he needs help assembling the circuit.

Each wire has an identifier (some lowercase letters) and can carry a 16-bit signal (a number from 0 to 65535). A signal is provided to each wire by a gate, another wire, or some specific value. Each wire can only get a signal from one source, but can provide its signal to multiple destinations. A gate provides no signal until all of its inputs have a signal.

The included instructions booklet describes how to connect the parts together: x AND y -> z means to connect wires x and y to an AND gate, and then connect its output to wire z.

For example:

123 -> x means that the signal 123 is provided to wire x.
x AND y -> z means that the bitwise AND of wire x and wire y is provided to wire z.
p LSHIFT 2 -> q means that the value from wire p is left-shifted by 2 and then provided to wire q.
NOT e -> f means that the bitwise complement of the value from wire e is provided to wire f.
Other possible gates include OR (bitwise OR) and RSHIFT (right-shift). If, for some reason, you'd like to emulate the circuit instead, almost all programming languages (for example, C, JavaScript, or Python) provide operators for these gates.

For example, here is a simple circuit:

123 -> x
456 -> y
x AND y -> d
x OR y -> e
x LSHIFT 2 -> f
y RSHIFT 2 -> g
NOT x -> h
NOT y -> i
After it is run, these are the signals on the wires:

d: 72
e: 507
f: 492
g: 114
h: 65412
i: 65079
x: 123
y: 456
In little Bobby's kit's instructions booklet (provided as your puzzle input), what signal is ultimately provided to wire a?
"""

from utils import load_input, print_answer

OPERATIONS = {
    "AND": "&",
    "OR": "|",
    "LSHIFT": "<<",
    "RSHIFT": ">>",
    "NOT": "^",
}

CIRCUITS = {}

input_data = load_input()
commands = input_data.split('\n')

def execute_command(command: str) -> None:
    value, target = command.split('->')

    try:
        CIRCUITS[target.strip()] = int(get_value(value.strip()))
    except TypeError:
        commands.append(command)
        pass


def get_value(command):
    match len(command.split(' ')):
        case 1:
            if command.strip().isdigit():
                return int(command)
            else:
                try:
                    return CIRCUITS[command.strip()]
                except KeyError:
                    return
        case 2:
            operation, operand = command.split(' ')
            try:
                operand = int(operand.strip()) if operand.strip().isdigit() else CIRCUITS[operand]
            except KeyError:
                return
            return eval(f'{65535}{OPERATIONS[operation]}{operand}')
        case 3:
            operand1, operation, operand2 = command.split(' ')
            try:
                operand1 = int(operand1.strip()) if operand1.strip().isdigit() else CIRCUITS[operand1]
            except KeyError:
                return
            try:
                operand2 = int(operand2.strip()) if operand2.strip().isdigit() else CIRCUITS[operand2]
            except KeyError:
                return
            return eval(f'{operand1} {OPERATIONS[operation]} {operand2}')


while commands:
    execute_command(commands[0])
    del commands[0]


first_answer = CIRCUITS['a']
overriden_input = load_input().replace('44430 -> b\n', '3176 -> b\n')
commands = overriden_input.split('\n')
CIRCUITS = {}
while commands:
    execute_command(commands[0])
    del commands[0]
second_answer = CIRCUITS['a']
print_answer(first_answer, second_answer)
