"""
--- Day 13: Knights of the Dinner Table ---
In years past, the holiday feast with your family hasn't gone so well. Not everyone gets along! This year, you resolve, will be different. You're going to find the optimal seating arrangement and avoid all those awkward conversations.

You start by writing up a list of everyone invited and the amount their happiness would increase or decrease if they were to find themselves sitting next to each other person. You have a circular table that will be just big enough to fit everyone comfortably, and so each person will have exactly two neighbors.

For example, suppose you have only four attendees planned, and you calculate their potential happiness as follows:

Alice would gain 54 happiness units by sitting next to Bob.
Alice would lose 79 happiness units by sitting next to Carol.
Alice would lose 2 happiness units by sitting next to David.
Bob would gain 83 happiness units by sitting next to Alice.
Bob would lose 7 happiness units by sitting next to Carol.
Bob would lose 63 happiness units by sitting next to David.
Carol would lose 62 happiness units by sitting next to Alice.
Carol would gain 60 happiness units by sitting next to Bob.
Carol would gain 55 happiness units by sitting next to David.
David would gain 46 happiness units by sitting next to Alice.
David would lose 7 happiness units by sitting next to Bob.
David would gain 41 happiness units by sitting next to Carol.
Then, if you seat Alice next to David, Alice would lose 2 happiness units (because David talks so much), but David would gain 46 happiness units (because Alice is such a good listener), for a total change of 44.

If you continue around the table, you could then seat Bob next to Alice (Bob gains 83, Alice gains 54). Finally, seat Carol, who sits next to Bob (Carol gains 60, Bob loses 7) and David (Carol gains 55, David gains 41). The arrangement looks like this:

     +41 +46
+55   David    02
Carol       Alice
+60    Bob    +54
     -7  +83
After trying every other seating arrangement in this hypothetical scenario, you find that this one is the most optimal, with a total change in happiness of 330.

What is the total change in happiness for the optimal seating arrangement of the actual guest list?

"""

from utils import load_input, print_answer
from collections import defaultdict
import itertools

guests = defaultdict(dict)
travel_distances = []


def create_guests(guest: str) -> None:
    name = guest.split(' ')[0]
    operator = '-' if 'lose' in guest else '+'
    value = guest.split(' ')[3]
    target = guest.split(' ')[-1][:-1]
    guests[name][target] = int(operator+value)

def calculate_happiness():
    overall_happiness = []
    for permutation in permutations:
        happiness = 0
        for i, guest in enumerate(permutation):
            try:
                r_neighbor = permutation[i-1]
            except IndexError:
                r_neighbor = permutation[-1]
            try:
                l_neighbor = permutation[i+1]
            except IndexError:
                l_neighbor = permutation[0]
            happiness += guests[guest][l_neighbor]
            happiness += guests[guest][r_neighbor]
        overall_happiness.append(happiness)
    return overall_happiness


def extend_guests():
    for guest in guests:
        guests[guest]['myself'] = 0
    guests['myself'] = {guest: 0 for guest in guests}
first_happiness = max(calculate_happiness())


for guest in load_input().split('\n'):
    create_guests(guest)


permutations = (list(itertools.permutations(guests.keys())))

extend_guests()
permutations = (list(itertools.permutations(guests.keys())))
print_answer(first_happiness, max(calculate_happiness()))