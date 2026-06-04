# Ordinal Suffix — Python Exercise #6

This project is based on Exercise #6 from the book *Python Programming Exercises, Gently Explained*.

Exercise Link:
https://inventwithpython.com/pythongently/exercise6/

---

# Overview

These Python programs determine the correct ordinal suffix for a number.

Examples:

1st
2nd
3rd
4th
11th
12th
13th
21st
22nd
23rd
101st

The exercise demonstrates how to handle special cases such as 11, 12, and 13, which use the suffix `th` instead of the usual `st`, `nd`, or `rd`.

---

# Files Included

## 1. `ordinal_suffix.py`

The original solution uses string operations to determine the correct suffix.

Features:

- Converts the number to a string
- Uses string slicing to inspect the last one or two digits
- Handles the special cases 11, 12, and 13
- Uses assertions to verify correctness

## 2. `ordinal_suffix_modulo.py`

An alternative implementation that uses modulo arithmetic instead of string slicing.

Features:

- Uses `% 100` to detect 11, 12, and 13
- Uses `% 10` to determine the final digit
- Uses assertions to verify correctness
- Demonstrates a more mathematical approach to the problem

---

# Comparing the Approaches

### String-Based Version

Advantages:

- Easy to read
- Good practice with strings and slicing
- Closely follows the original exercise

### Modulo Version

Advantages:

- Uses arithmetic instead of strings
- Efficient for numeric problems
- Demonstrates modulo operations

---

# Requirements

- Python 3

---

# Running the Programs

```bash
python3 ordinal_suffix.py
```

or

```bash
python3 ordinal_suffix_modulo.py
```

---

# Concepts Learned

- Functions
- Return values
- String conversion with `str()`
- String indexing
- String slicing
- Lists
- Conditional statements
- The modulo operator (`%`)
- Mathematical digit extraction
- Handling special cases
- Test assertions with `assert`
- Alternative problem-solving approaches

---

# Credits

Exercise based on:

*Python Programming Exercises, Gently Explained*
by Al Sweigart

https://inventwithpython.com/pythongently/
