# Temperature Conversion Projects — Python Exercise #2

These projects are based on Exercise #2 from the book *Python Programming Exercises, Gently Explained*.

Exercise Link:  
https://inventwithpython.com/pythongently/exercise2/

---

# Overview

This collection contains several versions of a temperature conversion program written in Python.

The projects gradually improve the original exercise by adding:

- Test assertions
- User input support
- Input validation
- f-strings for formatted output
- Cleaner number display with `:g`
- Decimal precision using Python's `decimal` library
- Decimal-specific error handling with `InvalidOperation`
- Proper rounding with `ROUND_HALF_UP`

---

# Files Included

## 1. `temperature_conversion.py`

The original exercise implementation with test assertions.

Features:

- Converts Celsius to Fahrenheit
- Converts Fahrenheit to Celsius
- Uses test assertions to verify correctness
- Uses f-strings to show which value is being tested

Source highlights:

```python
number = 0
print(f"Testing {number}...")
assert convertToCelsius(number) == -17.77777777777778
```

The final test also converts a Celsius value to Fahrenheit and then back to Celsius to make sure both functions work together.

---

## 2. `temperature_conversion_advanced.py`

An improved version that allows the user to enter temperatures interactively.

Features:

- User input support
- Unit selection (`C` or `F`)
- Basic validation
- Continuous prompt loop until valid input
- Uses `float()` for numeric input
- Catches `ValueError` when the user does not enter a valid number
- Uses f-strings with `:g` to print cleaner output without unnecessary trailing zeros

Example input:

```text
100 C
```

Example output formatting:

```python
print(f"{value:g}")
```

---

## 3. `temperature_conversion_advanced_decimal.py`

A more precise version using Python's `decimal` module.

Features:

- Uses `Decimal` instead of floating point numbers
- More accurate decimal calculations
- Uses `InvalidOperation` for Decimal-specific input errors
- Uses f-strings with `:g` after converting the Decimal result to `float` for cleaner display

Imports used:

```python
from decimal import Decimal, InvalidOperation
```

Decimal input handling:

```python
try:
    temperature = Decimal(parts[0])
    break
except InvalidOperation:
    print('Temperature must be a number')
```

Output formatting:

```python
print(f"{float(value):g}")
```

---

## 4. `temperature_conversion_advanced_decimal_round.py`

A final improved version with proper decimal rounding.

Features:

- Uses `Decimal`
- Uses `InvalidOperation` for Decimal-specific input errors
- Uses `ROUND_HALF_UP`
- Rounds results to two decimal places with `quantize()`
- Uses f-strings with `:g` for cleaner output
- More suitable for real-world numeric output

Imports used:

```python
from decimal import Decimal, InvalidOperation, ROUND_HALF_UP
```

Rounding example:

```python
return result.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)
```

Example rounded output:

```text
37.78
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
python3 temperature_conversion.py
```

or:

```bash
python3 temperature_conversion_advanced.py
```

or:

```bash
python3 temperature_conversion_advanced_decimal.py
```

or:

```bash
python3 temperature_conversion_advanced_decimal_round.py
```

---

# Example Usage

```text
Provide a temperature in Celsius or Fahrenheit which you want to convert
100 C
212.00
```

---

# Concepts Learned

These projects demonstrate:

- Functions
- Variables
- Test assertions with `assert`
- User input with `input()`
- Loops with `while True`
- Input validation
- Exception handling with `ValueError`
- Decimal-specific exception handling with `InvalidOperation`
- String manipulation with `split()` and `upper()`
- f-strings for formatted output
- Cleaner numeric display with `:g`
- Floating point vs decimal arithmetic
- Decimal rounding with `quantize()`
- `ROUND_HALF_UP` rounding

---

# Credits

Exercise based on:

*Python Programming Exercises, Gently Explained*  
by Al Sweigart

https://inventwithpython.com/pythongently/

