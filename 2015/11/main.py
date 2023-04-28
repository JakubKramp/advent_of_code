"""
--- Day 11: Corporate Policy ---
Santa's previous password expired, and he needs help choosing a new one.

To help him remember his new password after the old one expires, Santa has devised a method of coming up with a password based on the previous one. Corporate policy dictates that passwords must be exactly eight lowercase letters (for security reasons), so he finds his new password by incrementing his old password string repeatedly until it is valid.

Incrementing is just like counting with numbers: xx, xy, xz, ya, yb, and so on. Increase the rightmost letter one step; if it was z, it wraps around to a, and repeat with the next letter to the left until one doesn't wrap around.

Unfortunately for Santa, a new Security-Elf recently started, and he has imposed some additional password requirements:

Passwords must include one increasing straight of at least three letters, like abc, bcd, cde, and so on, up to xyz. They cannot skip letters; abd doesn't count.
Passwords may not contain the letters i, o, or l, as these letters can be mistaken for other characters and are therefore confusing.
Passwords must contain at least two different, non-overlapping pairs of letters, like aa, bb, or zz.
For example:

hijklmmn meets the first requirement (because it contains the straight hij) but fails the second requirement requirement (because it contains i and l).
abbceffg meets the third requirement (because it repeats bb and ff) but fails the first requirement.
abbcegjk fails the third requirement, because it only has one double letter (bb).
The next password after abcdefgh is abcdffaa.
The next password after ghijklmn is ghjaabcc, because you eventually skip all the passwords that start with ghi..., since i is not allowed.
Given Santa's current password (your puzzle input), what should his next password be?

Your puzzle input is hepxcrrq.

"""

import re
from utils import load_input, print_answer

consecutive_letters_regex = r'(?:abc|bcd|cde|def|efg|fgh|ghi|hij|ijk|jkl|klm|lmn|mno|nop|opq|pqr|qrs|rst|stu|tuv|uvw|vwx|wxy|xyz)'
forbidden_letters_regex = r'^(?:(?!i|l|o).)*$'
repeating_chars_regex = r'(\w)\1.*(\w)\2'


def check_password(password):
    return bool(re.search(consecutive_letters_regex, password)) and bool(re.search(forbidden_letters_regex, password)) and bool(re.search(repeating_chars_regex, password))


def increment_password(password):
    changed = ''
    counter = 1
    for letter in reversed(password):
        if letter == "z":
            changed += "a"
            counter += 1
        else:
            changed += chr(ord(letter) + 1)
            break
    return password[:-counter] + changed[::-1]


password = load_input()

while not check_password(password):
    password = increment_password(password)
first_password = password
password = increment_password(password)
while not check_password(password):
    password = increment_password(password)
second_password = password

print_answer(first_password, second_password)
