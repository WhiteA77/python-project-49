import random

RULE = "What number is missing in the progression?"


def generate_question():
    start = random.randint(1, 20)
    step = random.randint(2, 10)
    length = random.randint(5, 15)
    
    progression = []
    for i in range(length):
        progression.append(start + i * step)
    hidden_index = random.randint(0, length - 1)
    correct_answer = str(progression[hidden_index])
    progression[hidden_index] = ".."
    
    question = " ".join(map(str, progression))
    
    return question, correct_answer