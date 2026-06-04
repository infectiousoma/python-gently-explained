# Fizz Buzz — Python Exercise #5

This project is based on Exercise #5 from the book *Python Programming Exercises, Gently Explained*.

Exercise Link:  
https://inventwithpython.com/pythongently/exercise5/

---

# Overview

This Python program implements the classic Fizz Buzz programming exercise.

The program:

- Counts from `1` up to a user-provided number
- Prints `Fizz` for numbers divisible by `3`
- Prints `Buzz` for numbers divisible by `5`
- Prints `FizzBuzz` for numbers divisible by both `3` and `5`
- Prints the number itself when none of the conditions match

This exercise is commonly used to practice:

- Loops
- Conditional statements
- The modulo operator (`%`)
- Divisibility checks
- Function creation
- User input handling

---

# File Included

## `fizz_buzz.py`

Features:

- Uses a `for` loop with `range()`
- Uses modulo division to determine divisibility
- Uses `if`, `elif`, and `else` conditions
- Accepts user input
- Prints formatted output on a single line using `end=' '`

Main function:

```python
def fizzBuzz(upTo):
```

FizzBuzz condition:

```python
if number % 15 == 0:
```

The program checks divisibility by `15` first so numbers divisible by both `3` and `5` correctly print `FizzBuzz`.

---

# Visualizing the Logic

To help understand the program flow, the conditions can be visualized like this:

```text
Divisible by 15 -> FizzBuzz
Divisible by 3  -> Fizz
Divisible by 5  -> Buzz
Otherwise       -> Number
```

Example output up to 16:

```text
1 2 Fizz 4 Buzz Fizz 7 8 Fizz Buzz 11 Fizz 13 14 FizzBuzz 16
```

---

# Requirements

- Python 3

Download Python here:

https://www.python.org/downloads/

---

# Running the Program

Run the program from a terminal:

```bash
python3 fizz_buzz.py
```

---

# Example Usage

```text
Enter a number to try to get FizzBuzz
16
1 2 Fizz 4 Buzz Fizz 7 8 Fizz Buzz 11 Fizz 13 14 FizzBuzz 16
```

---

# Concepts Learned

This project demonstrates:

- Functions
- Loops with `for`
- The `range()` function
- Conditional statements
- The modulo operator (`%`)
- Divisibility testing
- User input with `input()`
- Integer conversion with `int()`
- Printing without line breaks using `end=' '`
- Basic program flow visualization

---

# Credits

Exercise based on:

*Python Programming Exercises, Gently Explained*  
by Al Sweigart

https://inventwithpython.com/pythongently/

