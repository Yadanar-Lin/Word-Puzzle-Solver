import pytest

from src.dictionary import load_words


def test_load_words(tmp_path):
    dictionary = tmp_path / "words.txt"
    dictionary.write_text(
        "apple\ncrane\nAPPLE\ncat\n12345\n",
        encoding="utf-8"
    )

    result = load_words(dictionary)

    assert result == ["APPLE", "CRANE"]


def test_missing_dictionary():
    with pytest.raises(FileNotFoundError):
        load_words("missing_dictionary.txt")


def test_empty_dictionary(tmp_path):
    dictionary = tmp_path / "words.txt"
    dictionary.write_text("", encoding="utf-8")

    assert load_words(dictionary) == []
