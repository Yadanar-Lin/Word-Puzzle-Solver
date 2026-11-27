import pytest

from src.solver import filter_candidates


def test_filter_candidates():
    candidates = ["CRANE", "SLATE", "TRACE", "BRAVE"]

    result = filter_candidates(
        candidates,"CRANE", ["G", "G", "G", "G", "G"])

    assert result == ["CRANE"]


def test_no_matching_candidates():
    candidates = ["SLATE", "BRAVE", "TRACE"]

    result = filter_candidates(
        candidates,
        "CRANE", ["G", "G", "G", "G", "G"])

    assert result == []


def test_multiple_matching_candidates():
    candidates = ["APPLE", "AMPLE", "ANGLE", "ALIEN"]

    result = filter_candidates(
        candidates, "APPLE", ["G", "B", "B", "B", "G"])

    assert result == []


def test_duplicate_letter_constraints():
    candidates = ["EERIE", "SPEED", "ELDER", "LEVEL"]

    result = filter_candidates(
        candidates, "SPEED", ["B", "B", "Y", "Y", "B"])

    assert "EERIE" in result
    assert "SPEED" not in result
