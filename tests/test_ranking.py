
import pytest

from src.ranking import calculate_entropy, rank_guesses


def test_entropy_for_single_candidate():
    assert calculate_entropy("CRANE", ["CRANE"]) == 0.0


def test_empty_candidates():
    with pytest.raises(ValueError):
        rank_guesses([])


def test_rank_guesses_returns_sorted_results():
    candidates = ["CRANE", "CRATE", "CRAZE"]

    results = rank_guesses(candidates)

    assert len(results) == 3

    scores = [score for word, score in results]

    assert scores == sorted(scores, reverse=True)


def test_non_candidate_guess():
    candidates = ["CRANE", "CRATE", "CRAZE"]
    possible_guesses = ["SLATE", "CRANE"]

    results = rank_guesses(candidates, possible_guesses)

    ranked_words = [word for word, score in results]

    assert "SLATE" in ranked_words
    assert "CRANE" in ranked_words


def test_entropy_is_nonnegative():
    candidates = ["CRANE", "CRATE", "CRAZE"]

    assert calculate_entropy("SLATE", candidates) >= 0
