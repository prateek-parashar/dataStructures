import string
from random import randint

target = "methinks it is like a weasel"
attempt = 0

def calculate_score(attempt, target):
    score = 0
    for i in range(len(target)):
        if attempt[i] == target[i]:
            score += 1
    return score / len(target)


def generate_monkey_type():
    available = list(string.ascii_lowercase)
    available.append(" ")
    result = []
    for i in range(len(target)):
        result.append(available[randint(0, len(available) - 1)])
    return result

best_score = 0
while True:
    score_so_far = calculate_score(generate_monkey_type(), target)
    if (score_so_far >= best_score):
        best_score = score_so_far
    attempt += 1
    if (score_so_far) == 1:
        print(f"WE GOT IT in {attempt} attempts!!!")
        break

    if attempt % 10000 == 0:
        print(f"We are still waiting, the number of attempts are {attempt}, the current best score is {best_score}")
