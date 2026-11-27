from src.feedback import generate_feedback


def filter_candidates(candidates, guess, feedback):
    remaining = []

    for candidate in candidates:
        candidate_feedback = generate_feedback(guess, candidate)

        if candidate_feedback == feedback:
            remaining.append(candidate)

    return remaining
