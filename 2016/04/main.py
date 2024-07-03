"""
--- Day 4: Security Through Obscurity ---
Finally, you come across an information kiosk with a list of rooms. Of course, the list is encrypted and full of decoy data, but the instructions to decode the list are barely hidden nearby. Better remove the decoy data first.

Each room consists of an encrypted name (lowercase letters separated by dashes) followed by a dash, a sector ID, and a checksum in square brackets.

A room is real (not a decoy) if the checksum is the five most common letters in the encrypted name, in order, with ties broken by alphabetization. For example:

aaaaa-bbb-z-y-x-123[abxyz] is a real room because the most common letters are a (5), b (3), and then a tie between x, y, and z, which are listed alphabetically.
a-b-c-d-e-f-g-h-987[abcde] is a real room because although the letters are all tied (1 of each), the first five are listed alphabetically.
not-a-real-room-404[oarel] is a real room.
totally-real-room-200[decoy] is not.
Of the real rooms from the list above, the sum of their sector IDs is 1514.

What is the sum of the sector IDs of the real rooms?

--- Part Two ---
With all the decoy data out of the way, it's time to decrypt this list and get moving.

The room names are encrypted by a state-of-the-art shift cipher, which is nearly unbreakable without the right software. However, the information kiosk designers at Easter Bunny HQ were not expecting to deal with a master cryptographer like yourself.

To decrypt a room name, rotate each letter forward through the alphabet a number of times equal to the room's sector ID. A becomes B, B becomes C, Z becomes A, and so on. Dashes become spaces.

For example, the real name for qzmt-zixmtkozy-ivhz-343 is very encrypted name.

What is the sector ID of the room where North Pole objects are stored?
"""

import re
from collections import Counter
from utils import load_input, print_answer


def is_real(room_name: str, checksum: str) -> bool:
    """
    Determines if room is real or not. The rule is if the checksum is the five most common letters
    in the encrypted name, in order, with ties broken by alphabetization the room is real
    :param room_name: Encrypted room name
    :param checksum: Five most common letters in encrypted room name
    :return: boolean indicating if the room is real or not
    """
    common_letters = sorted(Counter(room_name.replace('-', '')).items(), key=lambda letter: (-letter[1], letter[0]))
    expected_checksum = ''.join([letter[0] for letter in common_letters])[:5]
    return expected_checksum == checksum



def get_room_number(room_name: str) -> int:
    """
    This function returns sector ID if room is real, otherwise 0.
    :param room_name: Encrypted room name in format xxx-xxx-xxx-{SECTOR_ID}[CHECKSUM]
    :return: 0 If room is not real, Sector ID otherwise
    """
    pattern = r'(^[^\d]*)(\d+).*?\[([^\[\]]*)\]'
    name, sector_id, checksum = re.match(pattern, room_name).groups()
    return int(sector_id) if is_real(name, checksum) else 0

room_numbers = load_input().split('\n')

part_one = (sum([get_room_number(room_number) for room_number in room_numbers]))


def translate_letter(letter: str, rot: int) -> str:
    """
    Translate letter by a given number of places in a cesarean cipher
    :param letter: Letter to be translated
    :param rot: How many places in alphabet should be rotated
    :return: Translated letter
    """

    new_letter = ord(letter) + rot % 26
    return chr(new_letter) if new_letter <= 122 else chr(96 + new_letter % 122)

def ceasar_cipher(cipher_text: str, rot: int) -> str:
    """
    Decrypt ciphertext encoded using cesarean cip[her
    :param letter: Ciphertext to be translated
    :param rot: How many places in alphabet should be rotated
    :return: Plaintext
    """
    plaintext = ''.join([translate_letter(letter, rot) for letter in cipher_text])

    return plaintext.replace(chr(ord('-')+(rot % 26)), ' ')


def decrypt(room_name: str):
    pattern = r'(^[^\d]*)(\d+).*?\[([^\[\]]*)\]'
    cipher_text, rot, _ = re.match(pattern, room_name).groups()
    return ceasar_cipher(cipher_text, int(rot)), int(rot)

part_two = ''
for room_number in load_input().split('\n'):
    if decrypt(room_number)[0].strip() == 'northpole object storage':
        part_two = decrypt(room_number)[1]
        break

print_answer(part_one, part_two)