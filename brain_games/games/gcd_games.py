from random import randint

from brain_games.constants import GCD_INSTRUCTION
from brain_games.engine import run_game


def calc_correct_answer(num_1, num_2):
    if num_1 > num_2:
        num_1, num_2 = num_2, num_1
    
    divider = num_1
    while divider > 0:
        if num_1 % divider == 0 and num_2 % divider == 0:
            return divider
        else:
            divider -= 1


def get_numbers_and_answer():

    num_1 = randint(1, 100)
    num_2 = randint(1, 100)

    numbers = f'{num_1} {num_2}'
    correct_answer = calc_correct_answer(num_1, num_2)

    return numbers, correct_answer


def run_gcd_games():
    run_game(get_numbers_and_answer, GCD_INSTRUCTION)