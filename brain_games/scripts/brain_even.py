import random

import prompt


def greet():
    print("Welcome to the Brain Games!")


def is_even(number):
    return number % 2 == 0


def brain_even():
    name = prompt.string("May I have your name? ")
    print("Hello, " + name + "!")
    print('Answer "yes" if the number is even, otherwise answer "no".')

    correct_answers = 0

    while correct_answers < 3:
        number = random.randint(1, 100)
        print(f"Question: {number}")
        user_answer = prompt.string("Your answer: ")

        correct_answer = "yes" if is_even(number) else "no"

        if user_answer == correct_answer:
            print("Correct!")
            correct_answers += 1
        else:
            print(
                f"'{user_answer}' is wrong answer ;(. Correct answer was '{correct_answer}'."
            )
            print(f"Let's try again, {name}!")
            return

    print(f"Congratulations, {name}!")


def main():
    greet()
    brain_even()


if __name__ == "__main__":
    main()
