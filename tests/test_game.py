import pytest

from src.game import WordleGame


def test_correct_guess():
    game = WordleGame("APPLE")

    feedback = game.submit_guess("APPLE")

    assert feedback == ["G"] * 5
    assert game.won is True
    assert game.finished is True


def test_incorrect_guess():
    game = WordleGame("APPLE")

    feedback = game.submit_guess("CRANE")

    assert game.won is False
    assert game.finished is False
    assert game.attempts == 1


def test_max_attempts():
    game = WordleGame("APPLE", max_attempts=2)

    game.submit_guess("CRANE")
    game.submit_guess("SLATE")

    assert game.finished is True
    assert game.won is False
    assert game.attempts == 2


def test_guess_after_game_finished():
    game = WordleGame("APPLE")
    game.submit_guess("APPLE")

    with pytest.raises(ValueError):
        game.submit_guess("CRANE")


def test_invalid_guess():
    game = WordleGame("APPLE")

    with pytest.raises(ValueError):
        game.submit_guess("CAT")


def test_invalid_answer():
    with pytest.raises(ValueError):
        WordleGame("CAT")


def test_guess_history():
    game = WordleGame("APPLE")
    game.submit_guess("CRANE")

    assert len(game.history) == 1
    assert game.history[0][0] == "CRANE"
