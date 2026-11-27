
from collections import Counter


def generate_feedback(guess, answer):
    guess = guess.upper()
    answer = answer.upper()

    if len(guess) != 5 or len(answer) != 5:
        raise ValueError("Guess and answer should contain exactly 5 letters.")

    if not guess.isalpha() or not answer.isalpha():
        raise ValueError("Guess and answer should contain only letters.")

    feedback = ["B"] * 5
    remaining_letters = Counter(answer)

    for i in range(5):
        if guess[i] == answer[i]:
            feedback[i] = "G"
            remaining_letters[guess[i]] -= 1

    for i in range(5):
        if feedback[i] != "G" and remaining_letters[guess[i]] > 0:
            feedback[i] = "Y"
            remaining_letters[guess[i]] -= 1

    return feedback
