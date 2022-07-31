import random
import prompt

from brain_games.cli import greet_user

MAX_LIMIT = 3


def play():
    user_name = greet_user()
    print('Answer "yes" if the number is even, otherwise answer "no".')
    for _ in range(MAX_LIMIT):
        question, right_answer = get_question_answer()
        print(f'Question: {question}')
        user_answer = prompt.string('Your answer: ')
        if user_answer == right_answer:
            print('Correct!')
        else:
            print('{} is wrong answer ;(. Correct answer was {}'.format(
                user_answer, right_answer
            ))
            print(f"Let's try again, {user_name}")
            break
    else:
        print(f'Congratulations, {user_name}')


def get_question_answer():
    question = random.randint(1, 100)
    if question % 2 == 0:
        right_answer = 'yes'
    else:
        right_answer = 'no'
    return question, right_answer
