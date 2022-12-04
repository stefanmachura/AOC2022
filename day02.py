from helpers import get_file

ROCK = 1
PAPER = 2
SCISSORS = 3

FIGURES = {
    "A": ROCK,
    "B": PAPER,
    "C": SCISSORS,
    "X": ROCK,
    "Y": PAPER,
    "Z": SCISSORS,
}


def scoring(me, enemy):
    result = 0
    my_figure = FIGURES[me]
    enemy_figure = FIGURES[enemy]
    if my_figure == ROCK and enemy_figure == SCISSORS:
        result += 6
    if my_figure == PAPER and enemy_figure == ROCK:
        result += 6
    if my_figure == SCISSORS and enemy_figure == PAPER:
        result += 6

    if my_figure == enemy_figure:
        result += 3

    return result + my_figure


rounds = get_file("02")

score = 0
for round in rounds:
    enemy, me = round.split(" ")
    x = scoring(me, enemy)
    score += x

print(score)
