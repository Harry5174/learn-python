# Learn Python

Notes, exercises, and practice notebooks for learning Python step by step.

This repository documents the completed coursework for **The Complete Python Bootcamp From Zero to Hero in Python**, including notebook-based practice for problem solving and data structures.

## What's In This Repo

- Course notes and exercises in Jupyter notebooks
- Practice notebooks for LeetCode problems
- Data structures and algorithms explorations
- A lightweight `uv` setup for managing the Python environment

## Current Coverage

| Module | Topic |
|--------|-------|
| 01 | Python Object and Data Structure Basics |
| 02 | Python Statements |
| 03 | Methods and Functions |
| 04 | Milestone Project |
| 05 | Object Oriented Programming |
| 06 | Modules and Packages |
| 07 | Errors and Exception Handling |
| 08 | Milestone Project 2 |
| 09 | Built-in Functions |
| 10 | Python Decorators |
| 11 | Python Generators |
| 12 | Advanced Python Modules |
| 13 | Web Scraping |
| 14 | Working with Images |
| 15 | Working with PDFs and Spreadsheets |
| 16 | Emails with Python |
| 17 | Final Capstone Project |

## Repository Structure

```text
.
├── notebooks/
│   ├── 02-python-statements/
│   ├── 03-methods-functions/
│   ├── 04-milestone/
│   └── 05-object-oriented-programming/
├── leetcode/
└── data-structures-algorithms/
    ├── linked-lists/
    └── stack/
```

## Setup

This project uses [uv](https://github.com/astral-sh/uv) for dependency management and targets Python 3.13+.

```bash
uv sync
```

## Running The Notebooks

After syncing dependencies, open the notebooks in your preferred environment, for example:

```bash
uv run jupyter lab
```

If Jupyter is not installed in your environment yet, add it first:

```bash
uv add --dev jupyterlab
```
