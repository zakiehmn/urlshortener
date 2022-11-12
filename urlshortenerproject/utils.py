from random import choice
from string import ascii_letters, digits

AVAIABLE_CHARS = ascii_letters + digits

def create_random_slug(chars=AVAIABLE_CHARS, range_num=7):
    return "".join([choice(chars) for _ in range(range_num)])