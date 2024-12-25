from random import randint
from brain_games.engine import run_game
from brain_games.constants import PRIME_INSTRUCTION

def isprime(num):

    divider = num // 2 + 1
    if divider < 3:
        return True
        
    while divider > 2:
        if num % divider != 0:
            divider -= 1
        else:
            return False
    return True

def get_prime_nums_and_answer():

    random_num = randint(0, 50)
    question = str(random_num)
    correct_answer = "yes" if isprime(random_num) else "no"
    
    return question, correct_answer

def run_prime_games():
    run_game(get_prime_nums_and_answer, PRIME_INSTRUCTION)