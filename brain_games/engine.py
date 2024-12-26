import prompt


def run_game(question_and_answer, insructiom):
    name = prompt.string('Welcome to the Brain Games!\nMay I have your name? ')
    print(f'Hello, {name}!\n{insructiom}')

    for _ in range(3):
        question, correct_answer = question_and_answer()
        print(f'Question: {question}')
        user_answer = prompt.string('Your answer: ')

        if user_answer == str(correct_answer):
            print('Correct!')

        else:
            print(f"{user_answer} is wrong answer ;(. "
            f"Correct answer was {correct_answer}.\nLet's try again, {name}!")
            break
    else:
        print(f'Congratulations, {name}!')