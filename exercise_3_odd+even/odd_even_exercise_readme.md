# Odd & Even — Python Exercise #3

These projects are based on Exercise #3 from the book *Python Programming Exercises, Gently Explained*.

Exercise Link:  
https://inventwithpython.com/pythongently/exercise3/

---

# Overview

These Python programs determine whether a number is odd or even.

The projects gradually improve the original exercise by adding:

- Test assertions
- User input support
- Validation for numeric input
- Support for negative numbers
- Handling decimal numbers that are not whole integers
- f-strings for formatted output

---

# Files Included

## 1. `odd+even.py`

The original exercise implementation with test assertions.

Features:

- Determines whether a number is odd
- Determines whether a number is even
- Uses the modulo operator (`%`) to check divisibility by 2
- Uses test assertions to verify correctness
- Uses f-strings to show which value is being tested
- Tests positive numbers, negative numbers, and decimal values

Source highlights:

```python
result = (oddNumber % 2) == 1
```

```python
assert isEven(42) == True
```

The program tests several values including:

- Positive integers
- Negative integers
- Decimal numbers such as `3.1415`

---

## 2. `odd+even_advanced.py`

An improved version that allows the user to enter numbers interactively.

Features:

- User input support
- Validation for invalid numeric input
- Uses `float()` to accept decimal input
- Uses `ValueError` exception handling
- Detects non-whole numbers using `.is_integer()`
- Explains that decimal numbers are neither odd nor even
- Uses f-strings for formatted output

Input validation example:

```python
try:
    number = float(userInput)
except ValueError:
    print("You must enter a number")
```

Whole number validation:

```python
if not number.is_integer():
    print(f"{number} isn't a whole number so it's neither even nor odd")
```

Example interaction:

```text
Provide any number
7
7 is odd
```

Example decimal handling:

```text
Provide any number
3.1415
3.1415 isn't a whole number so it's neither even nor odd
```

---

# Requirements

- Python 3

Download Python here:

https://www.python.org/downloads/

---

# Running the Programs

Run either file from a terminal:

```bash
python3 odd+even.py
```

or:

```bash
python3 odd+even_advanced.py
```

---

# Concepts Learned

These projects demonstrate:

- Functions
- Boolean values (`True` and `False`)
- The modulo operator (`%`)
- Determining divisibility
- Test assertions with `assert`
- User input with `input()`
- Loops with `while True`
- Exception handling with `ValueError`
- Floating point numbers with `float()`
- Checking whether a decimal number is a whole integer
- Conditional statements with `if`, `elif`, and `else`
- f-strings for formatted output

---

# Credits

Exercise based on:

*Python Programming Exercises, Gently Explained*  
by Al Sweigart

https://inventwithpython.com/pythongently/

