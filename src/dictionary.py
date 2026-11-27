from pathlib import Path


def load_words(file_path=None):
    if file_path is None:
        file_path = Path(__file__).parent.parent / "data" / "words.txt"

    file_path = Path(file_path)

    if not file_path.exists():
        raise FileNotFoundError(f"Dictionary not found: {file_path}")

    with file_path.open("r", encoding="utf-8") as file:
        words = {
            word.strip().upper()
            for word in file
            if word.strip().isalpha() and len(word.strip()) == 5
        }

    return sorted(words)
