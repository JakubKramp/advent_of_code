"""
--- Day 16: Aunt Sue ---
Your Aunt Sue has given you a wonderful gift, and you'd like to send her a thank you card. However, there's a small problem: she signed it "From, Aunt Sue".

You have 500 Aunts named "Sue".

So, to avoid sending the card to the wrong person, you need to figure out which Aunt Sue (which you conveniently number 1 to 500, for sanity) gave you the gift. You open the present and, as luck would have it, good ol' Aunt Sue got you a My First Crime Scene Analysis Machine! Just what you wanted. Or needed, as the case may be.

The My First Crime Scene Analysis Machine (MFCSAM for short) can detect a few specific compounds in a given sample, as well as how many distinct kinds of those compounds there are. According to the instructions, these are what the MFCSAM can detect:

children, by human DNA age analysis.
cats. It doesn't differentiate individual breeds.
Several seemingly random breeds of dog: samoyeds, pomeranians, akitas, and vizslas.
goldfish. No other kinds of fish.
trees, all in one group.
cars, presumably by exhaust or gasoline or something.
perfumes, which is handy, since many of your Aunts Sue wear a few kinds.
In fact, many of your Aunts Sue have many of these. You put the wrapping from the gift into the MFCSAM. It beeps inquisitively at you a few times and then prints out a message on ticker tape:

children: 3
cats: 7
samoyeds: 2
pomeranians: 3
akitas: 0
vizslas: 0
goldfish: 5
trees: 3
cars: 2
perfumes: 1
You make a list of the things you can remember about each Aunt Sue. Things missing from your list aren't zero - you simply don't remember the value.

What is the number of the Sue that got you the gift?
"""

from utils import load_input, print_answer
import re
from collections import defaultdict
def default_aunt():
    keys = ['children','cats','samoyeds', 'pomeranians', 'akitas', 'vizslas', 'goldfish', 'trees', 'cars', 'perfumes' ]
    return {key: None for key in keys}

def match(aunt):
    target_aunt = {'children': 3,
                    'cats': 7,
                    'samoyeds': 2,
                    'pomeranians': 3,
                    'akitas': 0,
                    'vizslas': 0,
                    'goldfish': 5,
                    'trees': 3,
                    'cars': 2,
                    'perfumes': 1}
    for key in target_aunt.keys():
        if aunt[key] == None:
            pass
        elif target_aunt[key] != aunt[key]:
            return False
    return True

def match_ranges(aunt):
    target_aunt = {'children': 3,
                    'samoyeds': 2,
                    'akitas': 0,
                    'vizslas': 0,
                    'cars': 2,
                    'perfumes': 1}
    for key in target_aunt.keys():
        if aunt[key] == None:
            pass
        elif target_aunt[key] != aunt[key]:
            return False
    if aunt['cats'] == None:
        pass
    elif aunt['cats'] < 7:
        return False
    if aunt['trees'] == None:
        pass
    elif aunt['trees'] < 3:
        return False
    if aunt['pomeranians'] == None:
        pass
    elif aunt['pomeranians'] > 3:
        return False
    if aunt['goldfish'] == None:
        pass
    elif aunt['goldfish'] > 5:
        return False
    return True



aunts = defaultdict(default_aunt)

def create_aunts(aunt):
    id = int(re.search(r'(\d+(?=:))', aunt).group())
    keys = re.findall(r'[a-z]+(?=:)', aunt)
    values = list(map(int, re.findall(r'(?<=:\s)\d+', aunt)))
    for key, value in zip(keys,values):
        aunts[id][key] = value

for aunt in load_input().split('\n'):
    create_aunts(aunt)

matches = [(match(aunts[aunt]), aunt)for aunt in aunts if match(aunts[aunt])]
matches_range = [(match_ranges(aunts[aunt]), aunt)for aunt in aunts if match_ranges(aunts[aunt])]
print_answer(*[match[1] for match in matches_range])