
# Filter English words for the 5x5 word-search game.

from pathlib import Path


def filter_words():
    # File locations
    source = Path("data/english_words.txt")
    destination = Path("data/words.txt")

    # Read and filter words
    with source.open("r", encoding="utf-8") as file:
        words = {
            word.strip().upper()
            for word in file
            if word.strip().isalpha()
            and 3 <= len(word.strip()) <= 5
        }

    # Save filtered words alphabetically
    with destination.open("w", encoding="utf-8") as file:
        for word in sorted(words):
            file.write(word + "\n")

    print(f"Total filtered words: {len(words)}")
    print(f"Saved to: {destination}")


if __name__ == "__main__":
    filter_words()
