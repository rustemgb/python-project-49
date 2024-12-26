from random import randint

from brain_games.constants import PRIME_INSTRUCTION
from brain_games.engine import run_game


def isprime(num):
    if num < 3:
        return True
    
    divider = num // 2 + 1    
    while divider > 1:
        if num % divider != 0:
            divider -= 1
        else:
            return False
    return True


def get_prime_nums_and_answer():

    random_num = randint(1, 100)
    question = str(random_num)
    correct_answer = "yes" if isprime(random_num) else "no"
    
    return question, correct_answer


def run_prime_games():
    run_game(get_prime_nums_and_answer, PRIME_INSTRUCTION)