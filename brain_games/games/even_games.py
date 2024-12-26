from random import randint

from brain_games.constants import EVEN_INSTRUCTION
from brain_games.engine import run_game


def is_even(num):
    return num % 2 == 0


def get_random_num_and_answer():

    random_num = randint(1, 100)
    question = str(random_num)
    correct_answer = 'yes' if is_even(random_num) else 'no'
    
    return question, correct_answer


def run_even_game():
    run_game(get_random_num_and_answer, EVEN_INSTRUCTION)

