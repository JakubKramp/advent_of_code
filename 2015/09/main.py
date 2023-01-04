"""
--- Day 9: All in a Single Night ---
Every year, Santa manages to deliver all of his presents in a single night.

This year, however, he has some new locations to visit; his elves have provided him the distances between every pair of locations. He can start and end at any two (different) locations he wants, but he must visit each location exactly once. What is the shortest distance he can travel to achieve this?

For example, given the following distances:

London to Dublin = 464
London to Belfast = 518
Dublin to Belfast = 141
The possible routes are therefore:

Dublin -> London -> Belfast = 982
London -> Dublin -> Belfast = 605
London -> Belfast -> Dublin = 659
Dublin -> Belfast -> London = 659
Belfast -> Dublin -> London = 605
Belfast -> London -> Dublin = 982
The shortest of these is London -> Dublin -> Belfast = 605, and so the answer is 605 in this example.

What is the distance of the shortest route?
"""

from utils import load_input, print_answer
from collections import defaultdict
import itertools

distances = defaultdict(dict)
travel_distances = []

def set_distance(route: str) -> None:
    cities, distance = route.split('=')

    city, city1 = cities.split('to')
    city = city.strip()
    city1 = city1.strip()
    distances[city][city1] = int(distance)
    distances[city1][city] = int(distance)


for input in load_input().split('\n'):
    set_distance(input)
permutations = (list(itertools.permutations(distances.keys())))

def calculate_distance(order):
    distance = 0
    for current_city, destination in zip(order, order[1:]):
        distance += distances[current_city][destination]
    return distance

print_answer(min(list(map(calculate_distance, permutations))), max(list(map(calculate_distance, permutations))))
