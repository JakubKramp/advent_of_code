"""
--- Day 6: Probably a Fire Hazard ---
Because your neighbors keep defeating you in the holiday house decorating contest year after year, you've decided to deploy one million lights in a 1000x1000 grid.

Furthermore, because you've been especially nice this year, Santa has mailed you instructions on how to display the ideal lighting configuration.

Lights in your grid are numbered from 0 to 999 in each direction; the lights at each corner are at 0,0, 0,999, 999,999, and 999,0. The instructions include whether to turn on, turn off, or toggle various inclusive ranges given as coordinate pairs. Each coordinate pair represents opposite corners of a rectangle, inclusive; a coordinate pair like 0,0 through 2,2 therefore refers to 9 lights in a 3x3 square. The lights all start turned off.

To defeat your neighbors this year, all you have to do is set up your lights by doing the instructions Santa sent you in order.

For example:

turn on 0,0 through 999,999 would turn on (or leave on) every light.
toggle 0,0 through 999,0 would toggle the first line of 1000 lights, turning off the ones that were on, and turning on the ones that were off.
turn off 499,499 through 500,500 would turn off (or leave off) the middle four lights.
After following the instructions, how many lights are lit?
"""
import re

import numpy as np

from utils import load_input, print_answer

input_data = load_input()


def get_coordinates(command):
    coordinates = re.search(r'(\d+),(\d+).*(\d+),(\d+)', command).group().split(' through ')
    x = [int(coordinate.split(',')[0]) for coordinate in coordinates]
    y = [int(coordinate.split(',')[1]) for coordinate in coordinates]
    return x, y


def count_lit(input_data):
    grid = np.zeros((1000, 1000), dtype=bool)
    for command in input_data.split('\n'):
        x, y = get_coordinates(command)
        if command.startswith('turn off'):
            grid[x[0]-1:x[1], y[0]-1:y[1]] = np.zeros(((x[1]-x[0]+1), (y[1]-y[0]+1)), dtype=bool)
        elif command.startswith('turn on'):
            grid[x[0]-1:x[1], y[0]-1:y[1]] = np.ones(((x[1] - x[0]+1), (y[1] - y[0]+1)), dtype=bool)
        elif command.startswith('toggle'):
            grid[x[0]-1:x[1], y[0]-1:y[1]] = ~grid[x[0]-1:x[1], y[0]-1:y[1]]
        else:
            raise Exception
    return np.count_nonzero(grid)

def count_brightness(input_data):
    grid = np.zeros((1000, 1000), dtype=int)
    for command in input_data.split('\n'):
        x, y = get_coordinates(command)
        if command.startswith('turn off'):
            grid[x[0]-1:x[1], y[0]-1:y[1]] -= 1
        elif command.startswith('turn on'):
            grid[x[0]-1:x[1], y[0]-1:y[1]] += 1
        elif command.startswith('toggle'):
            grid[x[0]-1:x[1], y[0]-1:y[1]] += 2
        else:
            raise Exception
        grid[grid < 0] = 0
    return sum(sum(grid))


print_answer(count_lit(input_data), count_brightness(input_data))
