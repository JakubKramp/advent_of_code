"""
--- Day 22: Wizard Simulator 20XX ---
Little Henry Case decides that defeating bosses with swords and stuff is boring. Now he's playing the game with a wizard. Of course, he gets stuck on another boss and needs your help again.

In this version, combat still proceeds with the player and the boss taking alternating turns. The player still goes first. Now, however, you don't get any equipment; instead, you must choose one of your spells to cast. The first character at or below 0 hit points loses.

Since you're a wizard, you don't get to wear armor, and you can't attack normally. However, since you do magic damage, your opponent's armor is ignored, and so the boss effectively has zero armor as well. As before, if armor (from a spell, in this case) would reduce damage below 1, it becomes 1 instead - that is, the boss' attacks always deal at least 1 damage.

On each of your turns, you must select one of your spells to cast. If you cannot afford to cast any spell, you lose. Spells cost mana; you start with 500 mana, but have no maximum limit. You must have enough mana to cast a spell, and its cost is immediately deducted when you cast it. Your spells are Magic Missile, Drain, Shield, Poison, and Recharge.

Magic Missile costs 53 mana. It instantly does 4 damage.
Drain costs 73 mana. It instantly does 2 damage and heals you for 2 hit points.
Shield costs 113 mana. It starts an effect that lasts for 6 turns. While it is active, your armor is increased by 7.
Poison costs 173 mana. It starts an effect that lasts for 6 turns. At the start of each turn while it is active, it deals the boss 3 damage.
Recharge costs 229 mana. It starts an effect that lasts for 5 turns. At the start of each turn while it is active, it gives you 101 new mana.
Effects all work the same way. Effects apply at the start of both the player's turns and the boss' turns. Effects are created with a timer (the number of turns they last); at the start of each turn, after they apply any effect they have, their timer is decreased by one. If this decreases the timer to zero, the effect ends. You cannot cast a spell that would start an effect which is already active. However, effects can be started on the same turn they end.

For example, suppose the player has 10 hit points and 250 mana, and that the boss has 13 hit points and 8 damage:

-- Player turn --
- Player has 10 hit points, 0 armor, 250 mana
- Boss has 13 hit points
Player casts Poison.

-- Boss turn --
- Player has 10 hit points, 0 armor, 77 mana
- Boss has 13 hit points
Poison deals 3 damage; its timer is now 5.
Boss attacks for 8 damage.

-- Player turn --
- Player has 2 hit points, 0 armor, 77 mana
- Boss has 10 hit points
Poison deals 3 damage; its timer is now 4.
Player casts Magic Missile, dealing 4 damage.

-- Boss turn --
- Player has 2 hit points, 0 armor, 24 mana
- Boss has 3 hit points
Poison deals 3 damage. This kills the boss, and the player wins.
Now, suppose the same initial conditions, except that the boss has 14 hit points instead:

-- Player turn --
- Player has 10 hit points, 0 armor, 250 mana
- Boss has 14 hit points
Player casts Recharge.

-- Boss turn --
- Player has 10 hit points, 0 armor, 21 mana
- Boss has 14 hit points
Recharge provides 101 mana; its timer is now 4.
Boss attacks for 8 damage!

-- Player turn --
- Player has 2 hit points, 0 armor, 122 mana
- Boss has 14 hit points
Recharge provides 101 mana; its timer is now 3.
Player casts Shield, increasing armor by 7.

-- Boss turn --
- Player has 2 hit points, 7 armor, 110 mana
- Boss has 14 hit points
Shield's timer is now 5.
Recharge provides 101 mana; its timer is now 2.
Boss attacks for 8 - 7 = 1 damage!

-- Player turn --
- Player has 1 hit point, 7 armor, 211 mana
- Boss has 14 hit points
Shield's timer is now 4.
Recharge provides 101 mana; its timer is now 1.
Player casts Drain, dealing 2 damage, and healing 2 hit points.

-- Boss turn --
- Player has 3 hit points, 7 armor, 239 mana
- Boss has 12 hit points
Shield's timer is now 3.
Recharge provides 101 mana; its timer is now 0.
Recharge wears off.
Boss attacks for 8 - 7 = 1 damage!

-- Player turn --
- Player has 2 hit points, 7 armor, 340 mana
- Boss has 12 hit points
Shield's timer is now 2.
Player casts Poison.

-- Boss turn --
- Player has 2 hit points, 7 armor, 167 mana
- Boss has 12 hit points
Shield's timer is now 1.
Poison deals 3 damage; its timer is now 5.
Boss attacks for 8 - 7 = 1 damage!

-- Player turn --
- Player has 1 hit point, 7 armor, 167 mana
- Boss has 9 hit points
Shield's timer is now 0.
Shield wears off, decreasing armor by 7.
Poison deals 3 damage; its timer is now 4.
Player casts Magic Missile, dealing 4 damage.

-- Boss turn --
- Player has 1 hit point, 0 armor, 114 mana
- Boss has 2 hit points
Poison deals 3 damage. This kills the boss, and the player wins.
You start with 50 hit points and 500 mana points. The boss's actual stats are in your puzzle input. What is the least amount of mana you can spend and still win the fight? (Do not include mana recharge effects as "spending" negative mana.)
"""
import random


class Boss:
    hit_points: int
    damage: int
    poison: int = 0


    def __init__(self, hit_points: int, damage:int):
        self.hit_points = hit_points
        self.damage = damage

    def attack(self, target):
        target.hit_points -= (self.damage-target.armor)
        print(f'Boss attacks for {(self.damage-target.armor)}, target hp {target.hit_points}')

class Player:
    hit_points: int
    mana: int
    armor: int
    shield: int = 0
    recharge: int = 0
    spent: int = 0

    def __init__(self, hit_points: int, mana: int, armor: int = 0):
        self.hit_points = hit_points
        self.mana = mana
        self.armor = armor

    def magic_missile(self, target: Boss):
        self.mana -= 53
        self.spent += 53
        target.hit_points -= 4
        print(f'Player casts magic missile, player mana {self.mana}, target hp {target.hit_points}')

    def drain(self, target: Boss):
        self.mana -= 73
        self.spent += 73
        self.hit_points += 2
        target.hit_points -= 2
        print(f'Player casts drain, player mana {self.mana}, target hp {target.hit_points}, player hp {self.hit_points}')

    def cast_shield(self):
        self.mana -= 113
        self.spent += 113
        self.armor += 7
        self.shield = 6
        print(f'Player casts shield, player mana {self.mana}, player hp {self.hit_points}')

    def cast_recharge(self):
        self.recharge = 5
        self.mana -= 229
        self.spent += 229
        print(f'Player casts recharge, player mana {self.mana}, player hp {self.hit_points}')

    def cast_poison(self, target: Boss):
        target.poison = 6
        self.mana -=173
        self.spent += 173
        print(f'Player casts poison, player mana {self.mana}, target hp {target.hit_points}, player hp {self.hit_points}')

    def cast(self, target: Boss):

        if target.hit_points < 8 and target.poison:
            self.magic_missile(target)
            return

        if target.hit_points<5:
            self.magic_missile(target)
            return

        if not target.poison and target.hit_points >8:
            self.cast_poison(target)
            return

        if target.poison and not self.recharge and target.hit_points > 25 and self.mana< 300:
            self.cast_recharge()
            return

        if target.poison and not self.shield and self.hit_points < 40:
            self.cast_shield()
            return

        if self.hit_points < 5 and self.shield:
            self.drain(target)
            return
        self.magic_missile(target)

    def cast_random(self, boss):
        spells = ['missile', 'shield', 'drain', 'recharge', 'poison']
        spell = random.choice(spells)
        match spell:
            case 'missile':
                self.magic_missile(boss)
            case 'shield':
                self.cast_shield()
            case 'drain':
                self.drain(boss)
            case 'recharge':
                self.cast_recharge()
            case 'poison':
                self.cast_poison(boss)

def check_status(player, boss):
    if boss.poison:
        boss.hit_points -= 3
        boss.poison -= 1
        print(f'Poison hits boss for 3, it will be active for {boss.poison} more turns. Boss remaining hp {boss.hit_points}')
    if player.recharge:
        player.mana += 101
        player.recharge -= 1
        print(f'Recharge restores 101 mana, it will be active for {player.recharge} more turns.Player remaining mana {player.mana}')
    if player.shield:
        player.shield -= 1
        print(f'Shield last for {player.shield} more turns')
        if not player.shield:
            player.armor = 0


def end_turn(player, boss):
    player.cast(boss)
    check_status(player, boss)
    boss.attack(player)
    check_status(player, boss)

p = Player(50, 500)
b = Boss(51, 9)
"""
while b.hit_points > 0 and p.hit_points > 0:
    end_turn(p,b)
print(p.spent)

"""

def end_turn_hard(player, boss):
    player.hit_points -= 1
    check_status(player, boss)
    player.cast(boss)
    check_status(player, boss)
    boss.attack(player)

p = Player(50, 500)
b = Boss(51, 9)

def player_turn(player, boss):
    check_status(player, boss)
    player.cast_random(boss)

def boss_turn(player, boss):
    check_status(player, boss)
    boss.attack(player)


def would_win(player, boss):
    while boss.hit_points > 0 and player.hit_points > 0:
        player.hit_points -= 1
        if player.hit_points<1 or player.mana <54:
            return False
        player_turn(player, boss)
        if boss.hit_points<1:
            return True
        boss_turn(player, boss)
        if player.hit_points<1:
            return False

print(would_win(p,b))
winning_costs = []
for i in range(2000000):
    p = Player(50, 500)
    b = Boss(51, 9)
    if would_win(p, b):
        winning_costs.append(p.spent)
print(sorted(winning_costs))
# 1080 <answer< 1256
#answer!=1206|1156|1159|1196|1086|1144|1248|1242|1239