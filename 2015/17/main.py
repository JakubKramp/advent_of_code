"""
--- Day 17: No Such Thing as Too Much ---
The elves bought too much eggnog again - 150 liters this time. To fit it all into your refrigerator, you'll need to move it into smaller containers. You take an inventory of the capacities of the available containers.

For example, suppose you have containers of size 20, 15, 10, 5, and 5 liters. If you need to store 25 liters, there are four ways to do it:

15 and 10
20 and 5 (the first 5)
20 and 5 (the second 5)
15, 5, and 5
Filling all containers entirely, how many different combinations of containers can exactly fit all 150 liters of eggnog?
"""
from itertools import combinations
from utils import load_input, print_answer
bottles = list(map(int, load_input().split('\n')))
viable_combos = 0
four_bottle_combos = 0

for i in range(4,14):
    combos = combinations(bottles, i)
    for c in combos:
        if sum(c) == 150:
            viable_combos += 1

combos = combinations(bottles, 4)
for c in combos:
    if sum(c) == 150:
        four_bottle_combos += 1
print_answer(viable_combos, four_bottle_combos)

