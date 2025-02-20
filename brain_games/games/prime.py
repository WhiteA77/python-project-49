import random

RULE = "Answer \"yes\" if given number is prime. Otherwise answer \"no\"."


def prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


def generate_question():
    number = random.randint(1, 100)
    correct_answer = "yes" if prime(number) else "no"
    
    question = str(number)
    
    return question, correct_answer
