"""
--- Day 7: Internet Protocol Version 7 ---
While snooping around the local network of EBHQ, you compile a list of IP addresses (they're IPv7, of course; IPv6 is much too limited). You'd like to figure out which IPs support TLS (transport-layer snooping).

An IP supports TLS if it has an Autonomous Bridge Bypass Annotation, or ABBA. An ABBA is any four-character sequence which consists of a pair of two different characters followed by the reverse of that pair, such as xyyx or abba. However, the IP also must not have an ABBA within any hypernet sequences, which are contained by square brackets.

For example:

abba[mnop]qrst supports TLS (abba outside square brackets).
abcd[bddb]xyyx does not support TLS (bddb is within square brackets, even though xyyx is outside square brackets).
aaaa[qwer]tyui does not support TLS (aaaa is invalid; the interior characters must be different).
ioxxoj[asdfgh]zxcvbn supports TLS (oxxo is outside square brackets, even though it's within a larger string).
How many IPs in your puzzle input support TLS?

Your puzzle answer was 118.

--- Part Two ---
You would also like to know which IPs support SSL (super-secret listening).

An IP supports SSL if it has an Area-Broadcast Accessor, or ABA, anywhere in the supernet sequences (outside any square bracketed sections), and a corresponding Byte Allocation Block, or BAB, anywhere in the hypernet sequences. An ABA is any three-character sequence which consists of the same character twice with a different character between them, such as xyx or aba. A corresponding BAB is the same characters but in reversed positions: yxy and bab, respectively.

For example:

aba[bab]xyz supports SSL (aba outside square brackets with corresponding bab within square brackets).
xyx[xyx]xyx does not support SSL (xyx, but no corresponding yxy).
aaa[kek]eke supports SSL (eke in supernet with corresponding kek in hypernet; the aaa sequence is not related, because the interior character must be different).
zazbz[bzb]cdb supports SSL (zaz has no corresponding aza, but zbz has a corresponding bzb, even though zaz and zbz overlap).
"""

import re
from utils import load_input, print_answer

def support_tls(ip_address: str) -> bool:
    """
    Checks if given IP address supports TLS. An IP Address supports TLS is there is a sequence of four characters following pattern abba.
    However, if said pattern occurs inside of square brackets the address does not support TLS
    :param ip_address: An address to be checked
    :return: Boolean indicating if the rule is fulfilled or not
    """
    negative_regex = r'\[\w*(\w)(?!\1)(\w)\2\1\w*\]'
    positive_regex = r'\]?(\w)(?!\1)(\w)\2\1\w*\[?'

    if re.findall(negative_regex, ip_address):
        return False
    elif re.findall(positive_regex, ip_address):
        return True
    return False

def support_ssl(ip_address: str) -> bool:
    """
    Checks if given IP address supports SSL. An IP Address supports SSL is there is a sequence of three characters following pattern aba outside square brackets,
    and a corresponging sequence bab inside square brackets.
    :param ip_address: An address to be checked
    :return: Boolean indicating if the rule is fulfilled or not
    """
    negative_regex = r'(\[\w*(\w)(?!\2)(\w)\2\w*\])(\]?\3\2\3\[?)'
    positive_regex = r'(\]?\w*(\w)(?!\2)(\w)\2\w*\[?)(\[\w*\3\2\3\w*\])'

    if re.findall(negative_regex, ip_address):
        return False
    elif re.findall(positive_regex, ip_address):
        return True
    return False


ip_addresses = load_input().split('\n')
part_one = [support_tls(ip_address) for ip_address in ip_addresses].count(True)
print([support_tls(ip_address) for ip_address in ip_addresses].count(True))