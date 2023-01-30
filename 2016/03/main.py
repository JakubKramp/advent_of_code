"""
--- Day 3: Squares With Three Sides ---
Now that you can think clearly, you move deeper into the labyrinth of hallways and office furniture that makes up this part of Easter Bunny HQ. This must be a graphic design department; the walls are covered in specifications for triangles.

Or are they?

The design document gives the side lengths of each triangle it describes, but... 5 10 25? Some of these aren't triangles. You can't help but mark the impossible ones.

In a valid triangle, the sum of any two sides must be larger than the remaining side. For example, the "triangle" given above is impossible, because 5 + 10 is not larger than 25.

In your puzzle input, how many of the listed triangles are possible?
"""
import re
from utils import load_input, print_answer

valid_triangles=[]

def is_valid_triangle(dimensions):
    return dimensions[2] < dimensions[1]+dimensions[0]


def format_dimensions(dimensions):
    dimensions = re.findall(r'(\d+)', dimensions)
    dimensions = sorted(list(map(int, dimensions)))
    return dimensions


dims = load_input().split('\n')
formatted = list(map(format_dimensions, dims))

for i in range(int(len(dims)/3)):
    dim = load_input().split('\n')[i*3:(i+1)*3]
    nums = []
    for di in dim:
        num = re.findall(r'(\d+)', di)
        nums += num
    for j in range(3):
        nums = list(map(int, nums))
        print(sorted(nums[j::3]))
        valid_triangles.append(is_valid_triangle(sorted(nums[j::3])))

print_answer(list(map(is_valid_triangle, formatted)).count(True), valid_triangles.count(True))



