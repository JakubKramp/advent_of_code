"""
--- Day 9: Rope Bridge ---
This rope bridge creaks as you walk along it. You aren't sure how old it is, or whether it can even support your weight.

It seems to support the Elves just fine, though. The bridge spans a gorge which was carved out by the massive river far below you.

You step carefully; as you do, the ropes stretch and twist. You decide to distract yourself by modeling rope physics; maybe you can even figure out where not to step.

Consider a rope with a knot at each end; these knots mark the head and the tail of the rope. If the head moves far enough away from the tail, the tail is pulled toward the head.

Due to nebulous reasoning involving Planck lengths, you should be able to model the positions of the knots on a two-dimensional grid. Then, by following a hypothetical series of motions (your puzzle input) for the head, you can determine how the tail will move.

Due to the aforementioned Planck lengths, the rope must be quite short; in fact, the head (H) and tail (T) must always be touching (diagonally adjacent and even overlapping both count as touching):

....
.TH.
....

....
.H..
..T.
....

...
.H. (H covers T)
...
If the head is ever two steps directly up, down, left, or right from the tail, the tail must also move one step in that direction so it remains close enough:

.....    .....    .....
.TH.. -> .T.H. -> ..TH.
.....    .....    .....

...    ...    ...
.T.    .T.    ...
.H. -> ... -> .T.
...    .H.    .H.
...    ...    ...
Otherwise, if the head and tail aren't touching and aren't in the same row or column, the tail always moves one step diagonally to keep up:

.....    .....    .....
.....    ..H..    ..H..
..H.. -> ..... -> ..T..
.T...    .T...    .....
.....    .....    .....

.....    .....    .....
.....    .....    .....
..H.. -> ...H. -> ..TH.
.T...    .T...    .....
.....    .....    .....
You just need to work out where the tail goes as the head follows a series of motions. Assume the head and the tail both start at the same position, overlapping.

For example:

R 4
U 4
L 3
D 1
R 4
D 1
L 5
R 2
This series of motions moves the head right four steps, then up four steps, then left three steps, then down one step, and so on. After each step, you'll need to update the position of the tail if the step means the head is no longer adjacent to the tail. Visually, these motions occur as follows (s marks the starting position as a reference point):

== Initial State ==

......
......
......
......
H.....  (H covers T, s)

== R 4 ==

......
......
......
......
TH....  (T covers s)

......
......
......
......
sTH...

......
......
......
......
s.TH..

......
......
......
......
s..TH.

== U 4 ==

......
......
......
....H.
s..T..

......
......
....H.
....T.
s.....

......
....H.
....T.
......
s.....

....H.
....T.
......
......
s.....

== L 3 ==

...H..
....T.
......
......
s.....

..HT..
......
......
......
s.....

.HT...
......
......
......
s.....

== D 1 ==

..T...
.H....
......
......
s.....

== R 4 ==

..T...
..H...
......
......
s.....

..T...
...H..
......
......
s.....

......
...TH.
......
......
s.....

......
....TH
......
......
s.....

== D 1 ==

......
....T.
.....H
......
s.....

== L 5 ==

......
....T.
....H.
......
s.....

......
....T.
...H..
......
s.....

......
......
..HT..
......
s.....

......
......
.HT...
......
s.....

......
......
HT....
......
s.....

== R 2 ==

......
......
.H....  (H covers T)
......
s.....

......
......
.TH...
......
s.....
After simulating the rope, you can count up all of the positions the tail visited at least once. In this diagram, s again marks the starting position (which the tail also visited) and # marks other positions the tail visited:

..##..
...##.
.####.
....#.
s###..
So, there are 13 positions the tail visited at least once.

Simulate your complete hypothetical series of motions. How many positions does the tail of the rope visit at least once?
"""

class Stack:
    positions = []

    def add(self, coordinates):
        if len(self.positions) == 10:
            self.positions = self.positions[1:]
            self.positions.append(coordinates)


def load_input(filename: str = 'input.txt') -> str:
    with open(filename, 'r') as f:
        input_data = f.read()
    return input_data


class Snake:
    head_position = [0, 0]
    head_previous = [0, 0]
    tail_position = [0, 0]
    tail_visited = set()
    tail_visited.add((0, 0))

    def head_move(self, direction, length):
        if direction == 'U':
            for i in range(length):
                self.head_previous = self.head_position.copy()
                self.head_position[1] += 1
                if self.is_neighbor():
                    pass
                else:
                    self.tail_position = self.head_previous
                    self.tail_visited.add(tuple(self.tail_position))

        if direction == 'D':
            for i in range(length):
                self.head_previous = self.head_position.copy()
                self.head_position[1] -= 1
        if direction == 'L':
            for i in range(length):
                head_previous = self.head_position.copy()
                self.head_position[0] -= 1
                if self.is_neighbor():
                    pass
                else:
                    self.tail_position = head_previous
                    self.tail_visited.add(tuple(self.tail_position))
        if direction == 'R':
            for i in range(length):
                head_previous = self.head_position.copy()
                self.head_position[0] += 1
                if self.is_neighbor():
                    pass
                else:
                    self.tail_position = head_previous
                    self.tail_visited.add(tuple(self.tail_position))

    def is_neighbor(self):
        x_dist = abs(self.head_position[0] - self.tail_position[0])
        y_dist = abs(self.head_position[1] - self.tail_position[1])
        if x_dist < 2 and y_dist < 2:
            return True
        return False

    def tail_move(self):
        if self.is_neighbor():
            pass
        else:
            self.tail_position = self.head_previous
            self.tail_visited.add(tuple(self.tail_position))

    def run(self):
        for command in load_input().split('\n'):
            direction, length = command.split(' ')
            self.head_move(direction, int(length))
        return self.tail_visited


print(len(Snake.run()))
