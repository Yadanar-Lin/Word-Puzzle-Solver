from collections import Counter
from math import log2

from src.feedback import generate_feedback


def calculate_entropy(guess, candidates):
    if not candidates:
        raise ValueError("Candidates cannot be empty.")

    feedback_patterns = []

    for candidate in candidates:
        feedback = tuple(generate_feedback(guess, candidate))
        feedback_patterns.append(feedback)

    pattern_counts = Counter(feedback_patterns)
    total = len(candidates)

    entropy = 0.0

    for count in pattern_counts.values():
        probability = count / total
        entropy -= probability * log2(probability)

    return entropy


def rank_guesses(candidates, possible_guesses=None):
    if not candidates:
        raise ValueError("Candidates cannot be empty.")

    if possible_guesses is None:
        possible_guesses = candidates

    ranked = []

    for guess in set(word.upper() for word in possible_guesses):
        entropy = calculate_entropy(guess, candidates)
        ranked.append((guess, entropy))

    return sorted(ranked, key=lambda item: (-item[1], item[0]))
