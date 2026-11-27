from src.feedback import generate_feedback


class WordleGame:
    def __init__(self, answer, max_attempts=6):
        answer = answer.upper()

        if len(answer) != 5 or not answer.isalpha():
            raise ValueError("Answer must be exactly five letters.")

        if max_attempts < 1:
            raise ValueError("Maximum attempts must be at least 1.")

        self.answer = answer
        self.max_attempts = max_attempts
        self.attempts = 0
        self.history = []
        self.won = False
        self.finished = False

    def submit_guess(self, guess):
        guess = guess.upper()

        if self.finished:
            raise ValueError("Game is already finished.")

        if len(guess) != 5 or not guess.isalpha():
            raise ValueError("Guess must be exactly five letters.")

        feedback = generate_feedback(guess, self.answer)

        self.attempts += 1
        self.history.append((guess, feedback))

        if guess == self.answer:
            self.won = True
            self.finished = True
        elif self.attempts >= self.max_attempts:
            self.finished = True

        return feedback
