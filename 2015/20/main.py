"""

"""
from math import prod
from itertools import combinations

from utils import load_input, print_answer

input_data: int = int(load_input())


def factorize(n: int) -> list:
    i = 2
    factors = []
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)
    return factors


def sum_divisors(divisors: list) -> int:
    u = set(divisors)
    count = {uniq: divisors.count(uniq) for uniq in u}
    l = [int((num**(count+1)-1)/(num-1)) for num, count in count.items()]
    l.append(1)
    return prod(l)


def find_multiplication_combinations(numbers: list) -> list:
    result = set()
    for i in range(1, len(numbers)+1):
        for comb in combinations(numbers, i):
            result.add(prod(comb))
    return list(filter(lambda x: x > max(result)/50, result))
def day_1() -> int:
    max_num = 0
    house = 0
    # day 2
    while max_num < input_data/10:
        house += 1
        presents = sum_divisors(factorize(house))
        if max_num < presents:
            max_num = presents
        else:
            pass
    return house
def day_2() -> int:
    max_num = 0
    house = 0
    # day 2
    while max_num < input_data/11:
        house += 1
        presents = sum(find_multiplication_combinations(factorize(house)))
        if max_num < presents:
            max_num = presents
        else:
            pass
    return house

# Answer = 786241 - Too high
print_answer(day_1(), day_2())