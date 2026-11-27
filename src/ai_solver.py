from src.solver import filter_candidates
from src.ranking import rank_guesses


class WordleSolver:
    def __init__(self, candidates, allowed_guesses=None):
        self.candidates = sorted(set(
            word.upper() for word in candidates
        ))

        self.allowed_guesses = (
            sorted(set(word.upper() for word in allowed_guesses))
            if allowed_guesses is not None
            else self.candidates.copy()
        )

        self.history = []

    def update(self, guess, feedback):
        guess = guess.upper()

        self.history.append((guess, feedback.copy()))

        self.candidates = filter_candidates(
            self.candidates,
            guess,
            feedback
        )

        return self.candidates

    def recommend_guess(self):
        if not self.candidates:
            return None

        ranked = rank_guesses(
            self.candidates,
            self.allowed_guesses
        )

        return ranked[0][0]

    def get_candidates(self):
        return self.candidates.copy()
