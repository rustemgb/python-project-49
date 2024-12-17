import prompt

def run_game(game, insructiom):
    name = prompt.string('Welcome to the Brain Games!\nMay I have your name? ')
    print(f'Hello, {name}!\n{insructiom}')

    for _ in range(3):
        question, correct_answer = game()
        print(f'Question: {question}')
        user_answer = prompt.string('Your answer: ')

        if user_answer == correct_answer:
            print('Correct!')

        else:
            print(f"'yes' is wrong answer ;(. Correct answer was 'no'.\nLet's try again, {name}!")
        
            return
    
    print(f'Congratulations, {name}!')

        