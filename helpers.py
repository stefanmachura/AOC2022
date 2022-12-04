import string
from typing import List


def get_file(day: str) -> List:
    with open(f"day{day}.input", "r") as inp:
        input_list = inp.readlines()

    return [e.rstrip() for e in input_list]


def letter_to_value(in_letter: str) -> int:
    letter_values = {}
    for i, letter in enumerate(string.ascii_letters):
        letter_values[letter] = i + 1
    return letter_values[in_letter]
