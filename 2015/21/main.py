"""

"""
import math

from utils import load_input, print_answer
from itertools import combinations

class Item:
    name: str
    cost: int
    armor: int
    damage: int

    def __init__(self, item_name: str, cost: str, damage: str, armor: str):
        self.name = item_name
        self.cost = int(cost)
        self.armor = int(armor)
        self.damage = int(damage)

    def __eq__(self, other):
        if self.cost == other.cost:
            return True
        return False

    def __str__(self):
        return f'{self.name}, A:{self.armor}, D:{self.damage}, price {self.cost}'

    def __repr__(self):
        return f'{self.name}, A:{self.armor}, D:{self.damage}, price {self.cost}'


class Creature:
    hit_points: int
    damage: int
    armor: int

    def __init__(self, hit_points, damage, armor):
        self.hit_points = int(hit_points)
        self.damage = int(damage)
        self.armor = int(armor)

    def __str__(self):
        return f'HP:{self.hit_points}, A:{self.armor}, D:{self.damage}'


class Player:
    def __init__(self, hit_points, weapon=None, armor=None, ring_1=Item('Ring', 0, 0, 0), ring_2=Item('Ring', 0, 0, 0)):
        self.hit_points = int(hit_points)
        self.weapon = weapon
        self.armor_item = armor
        self.ring_1 = ring_1
        self.ring_2 = ring_2

    @property
    def damage(self):
        damage = 0
        if item := self.weapon:
            damage += item.damage
        if item := self.ring_1:
            damage += item.damage
        if item := self.ring_2:
            damage += item.damage
        return damage

    @property
    def armor(self):
        armor = 0
        if item := self.armor_item:
            armor += item.armor
        if item := self.ring_1:
            armor += item.armor
        if item := self.ring_2:
            armor += item.armor
        return armor

    @property
    def inventory_cost(self):
        cost = 0
        if item := self.weapon:
            cost += item.cost
        if item := self.armor_item:
            cost += item.cost
        if item := self.ring_1:
            cost += item.cost
        if item := self.ring_2:
            cost += item.cost
        return cost

    @property
    def rings(self):
        return [self.ring_1, self.ring_2]

    def upgrade_weapon_cost(self):
        if not self.weapon:
            return weapons[0].cost
        elif self.weapon == weapons[-1]:
            return 0
        else:
            return weapons[weapons.index(self.weapon)+1].cost - self.weapon.cost

    def upgrade_weapon(self):
        if not self.weapon:
            self.weapon = weapons[0]
        elif self.weapon == weapons[-1]:
            return 0
        else:
            self.weapon = weapons[weapons.index(self.weapon)+1]

    def upgrade_armor_cost(self):
        if not self.armor:
            return armor[0].cost
        elif self.armor == armor[-1]:
            return 0
        else:
            return armor[armor.index(self.armor_item)+1].cost - self.armor_item.cost

    def upgrade_armor(self):
        if not self.armor_item:
            self.armor_item = armor[0]
        elif self.armor_item == armor[-1]:
            return 0
        else:
            self.armor_item = armor[armor.index(self.armor_item)+1]

    def cheap_ring_upgrade(self):
        self.ring_1, self.ring_2 = ring_combinations[ring_combinations.index(self.rings)+1]

    def expensive_ring_upgrade(self):
        current_stats = sum_stats(self.rings)
        for i in range(ring_combinations.index(self.rings), len(ring_combinations)):
            stats = sum_stats(ring_combinations[i])
            if stats-current_stats>1:
                break
            else:
                e = ring_combinations[i]
        self.ring_1, self.ring_2 = e

    def ring_upgrade_cost(self):
        current_stats = sum_stats(self.rings)
        current_value = self.ring_1.cost+self.ring_2.cost
        c = ring_combinations[ring_combinations.index(self.rings)+1]
        cheap_value = sum_value(c)
        cheap = cheap_value-current_value
        for i in range(ring_combinations.index(self.rings), len(ring_combinations)):
            stats = sum_stats(ring_combinations[i])
            if stats-current_stats>1:
                break
            else:
                e = ring_combinations[i]
        expensive_value = sum_value(e)
        expensive = expensive_value - current_value
        return cheap, expensive

    def cheapest_upgrade_cost(self):
        return min([self.upgrade_weapon_cost(), self.upgrade_armor_cost(), self.ring_upgrade_cost()[0]])


    def most_expensive_upgrade(self):
        return max([self.upgrade_weapon_cost(), self.upgrade_armor_cost(), self.ring_upgrade_cost()[1]])

    def would_win(self, enemy):
        while self.hit_points > 0 and enemy.hit_points > 0:
            enemy.hit_points -= (self.damage - enemy.armor)
            print(f'Enemy HP {enemy.hit_points}')
            if enemy.hit_points < 1:
                return True
            self.hit_points -= (enemy.damage - self.armor)
            print(f'Your HP {self.hit_points}')
            if self.hit_points < 1:
                return False


def sum_value(rings):
    return rings[0].cost+rings[1].cost

def sum_stats(rings):
    return rings[0].armor+rings[1].armor+rings[0].damage+rings[1].damage


def create_inventory(inventory):
    weapons, armor, rings = inventory.split('\n\n')
    return create_rings(rings), create_items(weapons), create_items(armor)


def create_items(items: str) -> list:
    item_list = []
    items = items.split('\n')
    item_type = items[0].split(' ')[0][:-1]
    for item in items[1:]:
        stats = [stat for stat in item.split(' ') if stat]
        item_list.append(Item(*stats))
    return item_list


def create_rings(rings: str) -> list:
    ring_list = []
    rings = rings.split('\n')
    item_type = rings[0].split(' ')[0][:-1]
    for ring in rings[1:]:
        stats = [stat for stat in ring.split(' ') if stat]
        ring_list.append(Item(item_type, *stats[2:]))
    return ring_list

boss, inventory = load_input().split('\n\n\n')
stats = boss.split('\n')
boss_stats = [stat.split(':')[1] for stat in stats]
boss = Creature(*boss_stats)
rings, weapons, armor = create_inventory(inventory)
damage_rings = rings[0:3]
armor_rings = rings[3:]
ring_combinations = []
rings.append(Item('Ring', 0, 0, 0))
ring_combinations = list(combinations(rings, 2))
ring_combinations.append([Item('Ring', 0, 0, 0),Item('Ring', 0, 0, 0)])
ring_combinations = sorted(ring_combinations, key=lambda rings:((rings[0].cost+rings[1].cost), (rings[0].armor + rings[0].damage +rings[1].damage + rings[1].armor)))
