# Word Puzzle Solver

**CS152 — Programming Paradigms | San José State University**

A Python-based word puzzle solver that uses search algorithms and data structures to explore valid solutions to word-based puzzles.

## Project Overview

This project aims to develop an interactive word puzzle solver that systematically explores possible word combinations instead of returning a predetermined answer. It is designed to identify whether a puzzle has one solution, multiple solutions, or no valid solution.

## Project Objectives

- Represent word puzzles using appropriate Python data structures.
- Explore possible word combinations and placements using search-based problem solving.
- Prune invalid search paths to reduce unnecessary exploration.
- Validate possible solutions according to puzzle rules.
- Display all applicable solution outcomes clearly.

## AI Approach

The proposed solver uses a search-based approach to explore possible states and eliminate invalid paths. The implementation will investigate depth-first search (DFS), backtracking, and pruning.

- **State:** A partial puzzle configuration.
- **Actions:** Possible next word or letter placements.
- **Goal test:** Determine whether a completed configuration satisfies the puzzle rules.
- **Pruning:** Stop exploring paths that cannot produce valid solutions.

The exact puzzle representation and rules will be finalized during implementation.

## Expected Outcomes

| Outcome | Expected Behavior |
| --- | --- |
| One solution | Find and display the valid solution. |
| Multiple solutions | Find and display the valid possibilities. |
| No solution | Report that no valid solution exists. |

## Technologies

- Python 3
- Git and GitHub
- Search algorithms and Python data structures

## Team

- Yamini Karthik
- Yadanar Lin

## References

- Russell, S., & Norvig, P. (2020). *Artificial Intelligence: A Modern Approach* (4th ed.). Pearson.
- [Python Documentation](https://docs.python.org/3/)
