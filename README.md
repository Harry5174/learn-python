# Learn Python

Notes, exercises, and practice notebooks for learning Python step by step.

The repository is primarily organized around coursework from the Udemy course **The Complete Python Bootcamp From Zero to Hero in Python**, with additional notebook-based practice for problem solving and data structures.

## What's In This Repo

- Course notes and exercises in Jupyter notebooks
- Practice notebooks for LeetCode problems
- Data structures and algorithms explorations
- A lightweight `uv` setup for managing the Python environment

## Current Coverage

| Module | Topic | Status |
|--------|-------|--------|
| 01 | Python Object and Data Structure Basics | Planned |
| 02 | Python Statements | In repo |
| 03 | Methods and Functions | In repo |
| 04 | Milestone Project | In repo |
| 05 | Object Oriented Programming | In repo |
| 06 | Modules and Packages | Planned |
| 07 | Errors and Exception Handling | Planned |
| 08 | Milestone Project 2 | Planned |
| 09 | Built-in Functions | Planned |
| 10 | Python Decorators | Planned |
| 11 | Python Generators | Planned |
| 12 | Advanced Python Modules | Planned |
| 13 | Web Scraping | Planned |
| 14 | Working with Images | Planned |
| 15 | Working with PDFs and Spreadsheets | Planned |
| 16 | Emails with Python | Planned |
| 17 | Final Capstone Project | Planned |

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
