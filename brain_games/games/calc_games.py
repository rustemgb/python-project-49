from random import randint, choice
from brain_games.constants import CALC_INSTRUCTION, CALC_ARITHMETIC
from brain_games.engine import run_game

def calc_answer(num_1, num_2, arithmetic):
    if arithmetic == "+":
        return num_1 + num_2
    elif arithmetic == "-":
        return num_1 - num_2
    elif arithmetic == "*":
        return num_1 * num_2

def get_expression_and_answer():

    num_1 = randint(0, 30)
    num_2 = randint(0, 30)

    arithmetic = choice(CALC_ARITHMETIC)
    expression = f'{num_1} {arithmetic} {num_2}'
    correct_answer = calc_answer(num_1, num_2, arithmetic)

    return expression, correct_answer

def run_calc_game():
    run_game(get_expression_and_answer, CALC_INSTRUCTION)

