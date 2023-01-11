"""

"""

from utils import load_input, print_answer

dimensions = (6, 6)
always_lit = ((0, 0), (0, 5), (5, 0), (5, 0))

def get_initial_lit(input_data):
    lit_pre = set()
    for i in range(dimensions[0]):
        for j in range(dimensions[1]):
            if input_data[i][j] == '#':
                lit_pre.add((i, j))
    lit_pre.update(always_lit)
    return lit_pre


input_data = [list(line) for line in load_input().split('\n')]


def get_neighbours(x, y):
    neighbours = []
    for k in range(-1, 2):
        for l in range(-1, 2):
            if not (k or l) or x+k < 0 or y+l < 0 or x+k >= dimensions[0] or y + l >= dimensions[1]:
                pass
            else:
                neighbours.append((x+k, y+l))
    return set(neighbours)


def next_turn(lit_pre):
    lit_post = lit_pre.copy()
    for i in range(100):
        for j in range(100):
            if (i, j) in always_lit:
                pass
            else:
                lit_neighbours = len(lit_pre.intersection(get_neighbours(i, j)))
                if lit_neighbours == 3:
                    lit_post.add((i, j))
                elif (i, j) in lit_pre and lit_neighbours == 2:
                    pass
                else:
                    lit_post.discard((i, j))
    return lit_post

input_data = [list(line) for line in load_input().split('\n')]

test_data = """##.#.#
...##.
#....#
..#...
#.#..#
####.#""".split('\n')

currently_lit = get_initial_lit(test_data)
print(len(currently_lit))
for _ in range(5):
    currently_lit = next_turn(currently_lit)

print(len(currently_lit))