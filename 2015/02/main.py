"""
--- Day 2: I Was Told There Would Be No Math ---
The elves are running low on wrapping paper, and so they need to submit an order for more. They have a list of the dimensions (length l, width w, and height h) of each present, and only want to order exactly as much as they need.

Fortunately, every present is a box (a perfect right rectangular prism), which makes calculating the required wrapping paper for each gift a little easier: find the surface area of the box, which is 2*l*w + 2*w*h + 2*h*l. The elves also need a little extra paper for each present: the area of the smallest side.

For example:

A present with dimensions 2x3x4 requires 2*6 + 2*12 + 2*8 = 52 square feet of wrapping paper plus 6 square feet of slack, for a total of 58 square feet.
A present with dimensions 1x1x10 requires 2*1 + 2*10 + 2*10 = 42 square feet of wrapping paper plus 1 square foot of slack, for a total of 43 square feet.
All numbers in the elves' list are in feet. How many total square feet of wrapping paper should they order?
"""

import math

from utils import load_input, print_answer


def preprocess_data(input_data: str) -> list:
    dimensions = [dimensions.split('x') for dimensions in input_data.split('\n')]
    sorted_dimensions = [sorted(list(map(int, dimension))) for dimension in dimensions]
    return sorted_dimensions


def wrap(dimensions: list) -> int:
    return 3 * (dimensions[0] * dimensions[1]) + 2 * (dimensions[0] * dimensions[2]) + 2 * (dimensions[1] * dimensions[2])


def ribbon(dimensions: list) -> int:
    return 2 * dimensions[0] + 2 * dimensions[1] + math.prod(dimensions)


present_dimensions = preprocess_data(load_input())
required_wrap = list(map(wrap, present_dimensions))
required_ribbon = list(map(ribbon, present_dimensions))

print_answer(sum(required_wrap), sum(required_ribbon))
