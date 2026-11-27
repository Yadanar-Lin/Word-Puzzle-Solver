
import pytest

from src.feedback import generate_feedback


def test_all_green():
    assert generate_feedback("APPLE", "APPLE") == ["G", "G", "G", "G", "G"]


def test_all_gray():
    assert generate_feedback("ZZZZZ", "APPLE") == ["B", "B", "B", "B", "B"]


def test_mixed_feedback():
    assert generate_feedback("APPLE", "ALLEY") == ["G", "B", "B", "Y", "Y"]


def test_duplicate_letters():
    assert generate_feedback("SPEED", "EERIE") == ["B", "B", "Y", "Y", "B"]


def test_invalid_length():
    with pytest.raises(ValueError):
        generate_feedback("CAT", "APPLE")


def test_non_alphabetic_input():
    with pytest.raises(ValueError):
        generate_feedback("APP1E", "APPLE")
