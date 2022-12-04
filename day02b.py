from helpers import get_file

ROCK = 1
PAPER = 2
SCISSORS = 3

FIGURES = {
    "A": ROCK,
    "B": PAPER,
    "C": SCISSORS,
}

WIN = 6
DRAW = 3
LOST = 0

OUTCOME = {"X": LOST, "Y": DRAW, "Z": WIN}


def how_to_lose(enemy):
    if enemy == ROCK:
        return SCISSORS
    if enemy == PAPER:
        return ROCK
    if enemy == SCISSORS:
        return PAPER


def how_to_draw(enemy):
    return enemy


def how_to_win(enemy):
    if enemy == SCISSORS:
        return ROCK
    if enemy == PAPER:
        return SCISSORS
    if enemy == ROCK:
        return PAPER


HOW_TO = {LOST: how_to_lose, DRAW: how_to_draw, WIN: how_to_win}

SCORING = {how_to_lose: 0, how_to_draw: 3, how_to_win: 6}


def scoring(enemy, outcome):
    enemy_figure = FIGURES[enemy]
    outcome = OUTCOME[outcome]
    f = HOW_TO[outcome]
    score = SCORING[f]
    return f(enemy_figure) + score


rounds = get_file("02")

score = 0
for round in rounds:
    enemy, outcome = round.split(" ")
    score += scoring(enemy, outcome)

print(score)
