"""
--- Day 15: Science for Hungry People ---
Today, you set out on the task of perfecting your milk-dunking cookie recipe. All you have to do is find the right balance of ingredients.

Your recipe leaves room for exactly 100 teaspoons of ingredients. You make a list of the remaining ingredients you could use to finish the recipe (your puzzle input) and their properties per teaspoon:

capacity (how well it helps the cookie absorb milk)
durability (how well it keeps the cookie intact when full of milk)
flavor (how tasty it makes the cookie)
texture (how it improves the feel of the cookie)
calories (how many calories it adds to the cookie)
You can only measure ingredients in whole-teaspoon amounts accurately, and you have to be accurate so you can reproduce your results in the future. The total score of a cookie can be found by adding up each of the properties (negative totals become 0) and then multiplying together everything except calories.

For instance, suppose you have these two ingredients:

Butterscotch: capacity -1, durability -2, flavor 6, texture 3, calories 8
Cinnamon: capacity 2, durability 3, flavor -2, texture -1, calories 3
Then, choosing to use 44 teaspoons of butterscotch and 56 teaspoons of cinnamon (because the amounts of each ingredient must add up to 100) would result in a cookie with the following properties:

A capacity of 44*-1 + 56*2 = 68
A durability of 44*-2 + 56*3 = 80
A flavor of 44*6 + 56*-2 = 152
A texture of 44*3 + 56*-1 = 76
Multiplying these together (68 * 80 * 152 * 76, ignoring calories for now) results in a total score of 62842880, which happens to be the best score possible given these ingredients. If any properties had produced a negative total, it would have instead become zero, causing the whole score to multiply to zero.

Given the ingredients in your kitchen and their properties, what is the total score of the highest-scoring cookie you can make?
"""
from utils import load_input, print_answer
from itertools import permutations
class Ingredient:
    name: str
    capacity: int
    durability: int
    flavor: int
    texture: int
    calories: int

    def __init__(self, name, capacity, durability, flavor, texture, calories):
        self.name = name
        self.capacity = capacity
        self.durability = durability
        self.flavor = flavor
        self.texture = texture
        self.calories = calories

    def __str__(self):
        return f'{self.name}: capacity {self.capacity}, durability {self.durability}, flavor {self.flavor}, texture {self.texture}, calories {self.calories}'


ingredients = []


def create_ingredients(ingredient):
    name, values = ingredient.split(':')
    values = values.strip()
    values = [int(val.strip(',')) for val in values.split(' ') if not val.isalpha()]
    ingredients.append(Ingredient(name, *values).__dict__)

for input in load_input().split('\n'):
    create_ingredients(input)
possibilities = list(permutations(range(1, 100), 4))
possibilities = [possibility for possibility in possibilities if sum(possibility) == 100]
scores = []
fit_scores = []

for possibility in possibilities:
    capacity = possibility[0]*ingredients[0]['capacity'] + possibility[1]*ingredients[1]['capacity'] + possibility[2]*ingredients[2]['capacity'] + possibility[3]*ingredients[3]['capacity']
    capacity = capacity if capacity > 0 else 0
    durability = possibility[0]*ingredients[0]['durability'] + possibility[1]*ingredients[1]['durability'] + possibility[2]*ingredients[2]['durability'] + possibility[3]*ingredients[3]['durability']
    durability = durability if durability > 0 else 0
    flavor = possibility[0]*ingredients[0]['flavor'] + possibility[1]*ingredients[1]['flavor'] + possibility[2]*ingredients[2]['flavor'] + possibility[3]*ingredients[3]['flavor']
    flavor = flavor if flavor > 0 else 0
    texture = possibility[0]*ingredients[0]['texture'] + possibility[1]*ingredients[1]['texture'] + possibility[2]*ingredients[2]['texture'] + possibility[3]*ingredients[3]['texture']
    texture = texture if texture > 0 else 0
    calories = possibility[0]*ingredients[0]['calories'] + possibility[1]*ingredients[1]['calories'] + possibility[2]*ingredients[2]['calories'] + possibility[3]*ingredients[3]['calories']
    if calories == 500:
        fit_scores.append(capacity*durability*flavor*texture)
    else:
        scores.append(capacity*durability*flavor*texture)

print_answer(max(scores), max(fit_scores))

