"""
--- Day 14: Reindeer Olympics ---
This year is the Reindeer Olympics! Reindeer can fly at high speeds, but must rest occasionally to recover their energy. Santa would like to know which of his reindeer is fastest, and so he has them race.

Reindeer can only either be flying (always at their top speed) or resting (not moving at all), and always spend whole seconds in either state.

For example, suppose you have the following Reindeer:

Comet can fly 14 km/s for 10 seconds, but then must rest for 127 seconds.
Dancer can fly 16 km/s for 11 seconds, but then must rest for 162 seconds.
After one second, Comet has gone 14 km, while Dancer has gone 16 km. After ten seconds, Comet has gone 140 km, while Dancer has gone 160 km. On the eleventh second, Comet begins resting (staying at 140 km), and Dancer continues on for a total distance of 176 km. On the 12th second, both reindeer are resting. They continue to rest until the 138th second, when Comet flies for another ten seconds. On the 174th second, Dancer flies for another 11 seconds.

In this example, after the 1000th second, both reindeer are resting, and Comet is in the lead at 1120 km (poor Dancer has only gotten 1056 km by that point). So, in this situation, Comet would win (if the race ended at 1000 seconds).

Given the descriptions of each reindeer (in your puzzle input), after exactly 2503 seconds, what distance has the winning reindeer traveled?
"""

from utils import load_input, print_answer


class Reindeer:
    speed: int
    name: str
    runtime: int
    resttime: int

    def __init__(self, name, speed, runtime, resttime):
        self.name = name
        self.speed = int(speed)
        self.runtime = int(runtime)
        self.resttime = int(resttime)

    def __repr__(self):
        return f'{self.name}, can fly {self.speed} km/s for {self.runtime}, has to rest {self.resttime} afterwards'

    @property
    def one_cycle_distance(self):
        return self.speed * self.runtime

    def distance(self, second):
        cycle = int(second/(self.runtime+self.resttime))
        distance = self.one_cycle_distance * cycle
        current_time = second % (self.runtime+self.resttime)
        if current_time >= self.runtime:
            distance += self.speed*self.runtime
        else:
            distance += self.speed*current_time
        return distance


def create_reindeer(reindeer):
    data = reindeer.split(' ')
    return Reindeer(data[0], data[3], data[6], data[13])


reindeers = [create_reindeer(reindeer)for reindeer in load_input().split('\n')]
distances = [reindeer.distance(2053) for reindeer in reindeers]


points = {reindeer.name: 0 for reindeer in reindeers}
for i in range(1,2504):
    distances = {reindeer.name: reindeer.distance(i) for reindeer in reindeers}
    max_value = max(distances.values())
    winners = [reindeer for reindeer in distances if distances[reindeer] == max_value]
    for winner in winners:
        points[winner] += 1

print_answer(max(distances.values()), max(points.values()))
