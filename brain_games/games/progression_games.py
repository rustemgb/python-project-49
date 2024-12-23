from random import randint
from brain_games.engine import run_game
from brain_games.constants import PROGRESSION_INSTRUCTION


def get_progression_nums_and_answer():
    
    start = randint(0, 10)
    step = randint(1, 10)
    length = 10

    progression = []
    for i in range(length):
        progression.append(start + step * i)

    hidden_index = randint(0, length - 1)
    correct_answer = progression[hidden_index]
    progression[hidden_index] = ".."
    question = ' '.join(map(str, progression))

    return question, correct_answer


def run_progression_games():
    run_game(get_progression_nums_and_answer, PROGRESSION_INSTRUCTION)
