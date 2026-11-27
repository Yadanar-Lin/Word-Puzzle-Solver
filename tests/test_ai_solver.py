import pytest

from src.ai_solver import WordleSolver
from src.feedback import generate_feedback


def test_initial_candidates():
    solver = WordleSolver(["APPLE", "CRANE", "SLATE"])

    assert solver.get_candidates() == ["APPLE", "CRANE", "SLATE"]


def test_update_candidates():
    candidates = ["APPLE", "CRANE", "SLATE"]

    solver = WordleSolver(candidates)

    feedback = generate_feedback("APPLE", "APPLE")
    result = solver.update("APPLE", feedback)

    assert result == ["APPLE"]


def test_recommend_guess():
    solver = WordleSolver(["CRANE", "CRATE", "CRAZE"])

    recommendation = solver.recommend_guess()

    assert recommendation in ["CRANE", "CRATE", "CRAZE"]


def test_recommendation_with_no_candidates():
    solver = WordleSolver(["APPLE"])

    solver.update("APPLE", ["B"] * 5)

    assert solver.recommend_guess() is None


def test_history():
    solver = WordleSolver(["APPLE", "CRANE"])

    feedback = generate_feedback("APPLE", "APPLE")
    solver.update("APPLE", feedback)

    assert len(solver.history) == 1


def test_non_candidate_guess_recommendation():
    candidates = ["CRANE", "CRATE", "CRAZE"]
    allowed = ["SLATE", "CRANE", "CRATE", "CRAZE"]

    solver = WordleSolver(candidates, allowed)

    assert solver.recommend_guess() in allowed
