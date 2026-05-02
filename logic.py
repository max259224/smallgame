import random

def generate_answer(start=1, end=100):
    return random.randint(start, end)

def check_guess(guess, answer):
    if guess > answer:
        return "too_high"
    elif guess < answer:
        return "too_low"
    else:
        return "correct"
