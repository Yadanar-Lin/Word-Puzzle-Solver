# Word Puzzle Solver

**CS152 — Programming Paradigms | San José State University**

A Python-based Wordle-style puzzle game that uses AI search techniques and data structures to help users solve word puzzles through intelligent guess recommendations.

## Project Overview

This project aims to develop an interactive Wordle-style game where users attempt to guess a hidden word. After each guess, the game provides feedback indicating which letters are correct, misplaced, or incorrect. The AI uses this feedback to narrow down possible words and recommend the next guess.

The system explores possible solutions based on previous guesses rather than providing predetermined recommendations. It is designed to handle situations where one, multiple, or no possible words remain.

## Project Objectives

- Represent words, guesses, and feedback using appropriate Python data structures.
- Allow users to enter guesses and receive feedback.
- Narrow down possible words based on previous guesses.
- Recommend the next guess using search-based problem solving.
- Eliminate invalid candidates to reduce unnecessary exploration.
- Display possible solutions and AI recommendations clearly.

## AI Approach

The proposed system uses constraint-based search to explore possible words and eliminate candidates that do not match previous feedback. The AI will investigate candidate filtering, search strategies, and guess ranking to recommend useful guesses.

- **State:** The remaining possible words and previous guess feedback.
- **Actions:** Select a possible word as the next guess.
- **Goal test:** Determine whether the guessed word matches the hidden word.
- **Pruning:** Eliminate words that are inconsistent with previous feedback.

The exact search and recommendation strategies will be finalized during implementation.

## Expected Outcomes

| Outcome | Expected Behavior |
| --- | --- |
| One solution | Identify the remaining possible word and recommend it. |
| Multiple solutions | Display possible words and recommend a useful next guess. |
| No solution | Report that no possible words match the current constraints. |

## Technologies

- Python 3
- Git and GitHub
- Search algorithms and Python data structures
- Graphical user interface (optional)

## Team

- Yamini Karthik
- Yadanar Lin

## References

- Russell, S., & Norvig, P. (2020). *Artificial Intelligence: A Modern Approach* (4th ed.). Pearson.
- [Python Documentation](https://docs.python.org/3/)
- dwyl/english-words — Open-source English word list used for dictionary validation and AI word recommendations.
