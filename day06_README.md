# Day 6 — String Methods (upper, lower, replace, split)
### Practice Problems & Solutions

This folder contains solutions to the 7 practice problems from **Day 6** of the
**100 Days of Python Challenge**, covering common built-in string methods:
`.upper()`, `.lower()`, `.replace()`, `.split()`, and `.strip()`.

---

## Problem 1 — Uppercase Conversion
**File:** [`day06_problem1_uppercase.py`](./day06_problem1_uppercase.py)

Converts a lowercase name to uppercase using `.upper()`.

## Problem 2 — Replace a Word
**File:** [`day06_problem2_replace_word.py`](./day06_problem2_replace_word.py)

Replaces one word in a sentence with another using `.replace()`.

## Problem 3 — Split by Comma
**File:** [`day06_problem3_split_comma.py`](./day06_problem3_split_comma.py)

Splits a comma-separated string into a list using `.split(",")`.

## Problem 4 — Strip Extra Spaces
**File:** [`day06_problem4_strip_spaces.py`](./day06_problem4_strip_spaces.py)

Removes leading/trailing whitespace from user input using `.strip()`,
showing the value before and after.

## Problem 5 — Case-Insensitive Match
**File:** [`day06_problem5_case_insensitive_match.py`](./day06_problem5_case_insensitive_match.py)

Normalizes user input with `.lower()` before comparing it, so "Yes",
"YES", and "yes" are all treated the same.

## Problem 6 — Debug Challenge
**File:** [`day06_problem6_debug_challenge.py`](./day06_problem6_debug_challenge.py)

Fixes a bug where `.upper()`'s result was never saved back to a
variable, so the change appeared to have no effect.

## Problem 7 — Text Cleaner / Slug Generator
**File:** [`day06_problem7_text_cleaner_slug.py`](./day06_problem7_text_cleaner_slug.py)

Chains `.strip()`, `.lower()`, and `.replace()` together to turn a
sentence into a URL-friendly "slug".

---

### 🔑 Key Concepts Practiced
- String methods return new strings; they don't modify the original
- `.upper()` / `.lower()` for case conversion
- `.replace(old, new)` for substituting text
- `.split(separator)` for breaking a string into a list
- `.strip()` for removing leading/trailing whitespace
- Chaining multiple string methods together

---

**Part of the [100 Days of Python Challenge](#)** 🐍
