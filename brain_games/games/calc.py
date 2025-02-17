import random

RULE = "What is the result of the expression?"


def generate_question():
    num1 = random.randint(1, 50)
    num2 = random.randint(1, 50)
    operator = random.choice(['+', '-', '*'])
    
    question = f"{num1} {operator} {num2}"
    answer = str(eval(question))
    
    return question, answer