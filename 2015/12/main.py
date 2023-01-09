"""
--- Day 12: JSAbacusFramework.io ---
Santa's Accounting-Elves need help balancing the books after a recent order. Unfortunately, their accounting software uses a peculiar storage format. That's where you come in.

They have a JSON document which contains a variety of things: arrays ([1,2,3]), objects ({"a":1, "b":2}), numbers, and strings. Your first job is to simply find all of the numbers throughout the document and add them together.

For example:

[1,2,3] and {"a":2,"b":4} both have a sum of 6.
[[[3]]] and {"a":{"b":4},"c":-1} both have a sum of 3.
{"a":[-1,1]} and [-1,{"a":1}] both have a sum of 0.
[] and {} both have a sum of 0.
You will not encounter any strings containing numbers.

What is the sum of all numbers in the document?
"""
import json

from utils import load_input, print_answer
import re

input_data = load_input()
red_dict = r'\{([^{]*:"red"[^}]*)\}'
numbers = [int(num) for num in re.findall(r'(-?\d*)', input_data) if num]

def parse(input_data):
    opened = 0
    closed = 0
    seq = ''
    for i in input_data:
        if i == '{':
            opened += 1
        elif i == '}':
            closed += 1
        if opened:
            seq += i
        if opened == closed and opened !=0:
            opened = 0
            closed = 0

            if 'red' in json.loads(seq).values():
                dicts.append(seq)
            else:
                parse(seq[1:-1])
            seq = ''
    return dicts


dicts = []
dicts = parse(input_data)

for dic in dicts:
    input_data = input_data.replace(dic, '')

excluded = [int(num) for num in re.findall(r'(-?\d*)', input_data) if num]


print_answer(sum(numbers), sum(excluded))
