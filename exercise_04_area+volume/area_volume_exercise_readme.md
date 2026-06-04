# Area & Volume — Python Exercise #4

These projects are based on Exercise #4 from the book *Python Programming Exercises, Gently Explained*.

Exercise Link:  
https://inventwithpython.com/pythongently/exercise4/

---

# Overview

These Python programs calculate:

- Area
- Perimeter
- Volume
- Surface Area

The projects gradually improve the original exercise by adding:

- Test assertions
- Organized automated test lists
- User input support
- Validation for numeric input
- Decimal precision using Python's `decimal` library
- Decimal-specific exception handling
- Rounding with `ROUND_HALF_UP`
- f-strings for formatted output
- Formula explanations shown to the user
- Cleaner numeric formatting with `:g`

---

# Files Included

## 1. `area+volume.py`

The original exercise implementation with direct test assertions.

Features:

- Calculates area
- Calculates perimeter
- Calculates volume
- Calculates surface area
- Uses functions for each calculation
- Uses test assertions to verify correctness
- Uses f-strings to show test information

Functions included:

```python
area(length, width)
perimeter(length, width)
volume(length, width, height)
surfaceArea(length, width, height)
```

Formula examples:

```python
result = (length * width)
```

```python
result = ((length * width) + (length * height) + (width * height)) * 2
```

The tests include:

- Standard dimensions
- Zero values
- Larger numbers

---

## 2. `area+volume_tests.py`

A reorganized testing version using grouped test lists and loops.

Features:

- Stores tests in lists of tuples
- Uses loops to run repeated tests automatically
- Cleaner and more scalable testing structure
- Uses assertions for validation
- Uses f-strings for formatted output

Example test structure:

```python
areaTests = [
    (10, 10, 100),
    (0, 9999, 0),
    (5, 8, 40)
]
```

Looped testing example:

```python
for length, width, expected in areaTests:
    assert area(length, width) == expected
```

---

## 3. `area+volume_advanced.py`

An interactive version that allows the user to enter dimensions.

Features:

- User input support
- Input validation
- Uses `float()` for decimal values
- Uses `ValueError` exception handling
- Displays formulas used in calculations
- Uses f-strings for formatted output
- Uses `:g` formatting for cleaner numeric display

Input example:

```text
10 5 2
```

Example formula output:

```text
The area of your object is calculated with: lw | 10 * 5
```

Output formatting example:

```python
print(f"The area is {area(length, width):g}")
```

---

## 4. `area+volume_advanced_decimal.py`

A Decimal-based version for more accurate arithmetic.

Features:

- Uses `Decimal` instead of floating point numbers
- More precise decimal calculations
- Uses `InvalidOperation` for Decimal-specific input errors
- Uses f-strings with `:g` formatting
- Preserves the interactive formula display

Imports used:

```python
from decimal import Decimal, InvalidOperation
```

Decimal input handling:

```python
try:
    length = Decimal(parts[0])
except InvalidOperation:
    print("Values must be numbers")
```

---

## 5. `area+volume_advanced_decimal_round.py`

A final improved version with Decimal rounding support.

Features:

- Uses `Decimal`
- Uses `InvalidOperation`
- Uses `ROUND_HALF_UP`
- Rounds results to two decimal places using `quantize()`
- Uses f-strings and `:g` formatting
- More suitable for real-world numeric calculations

Imports used:

```python
from decimal import Decimal, InvalidOperation, ROUND_HALF_UP
```

Rounding example:

```python
result = result.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)
```

---

# Requirements

- Python 3

Download Python here:

https://www.python.org/downloads/

---

# Running the Programs

Run any file from a terminal:

```bash
python3 area+volume.py
```

or:

```bash
python3 area+volume_tests.py
```

or:

```bash
python3 area+volume_advanced.py
```

or:

```bash
python3 area+volume_advanced_decimal.py
```

or:

```bash
python3 area+volume_advanced_decimal_round.py
```

---

# Example Usage

```text
Please enter the length, width, and height of the object.
10 5 2

The area of your object is calculated with: lw | 10 * 5
The area is 50
```

---

# Concepts Learned

These projects demonstrate:

- Functions
- Mathematical formulas
- Area, perimeter, volume, and surface area calculations
- Variables
- Arithmetic operators
- The order of operations
- Test assertions with `assert`
- Organizing automated tests with lists and loops
- User input with `input()`
- Loops with `while True`
- Exception handling with `ValueError`
- Decimal-specific exception handling with `InvalidOperation`
- Floating point arithmetic with `float()`
- Decimal arithmetic with `Decimal`
- Decimal rounding with `quantize()`
- `ROUND_HALF_UP` rounding
- String formatting with f-strings
- Cleaner numeric display with `:g`

---

# Credits

Exercise based on:

*Python Programming Exercises, Gently Explained*  
by Al Sweigart

https://inventwithpython.com/pythongently/

