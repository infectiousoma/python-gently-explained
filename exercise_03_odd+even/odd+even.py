def isOdd(oddNumber):
  result = (oddNumber % 2) == 1
  return result

def isEven(evenNumber):
  result = (evenNumber % 2) == 0
  return result

number = 42
print(F"Testing if {number} is Odd...")
assert isOdd(number) == False
print("False!")

number = 9999
print(F"Testing if {number} is Odd...")
assert isOdd(number) == True
print("True!")

number = -10
print(F"Testing if {number} is Odd...")
assert isOdd(number) == False
print("False!")

number = -11
print(F"Testing if {number} is Odd...")
assert isOdd(number) == True
print("True!")

number = 3.1415
print(F"Testing if {number} is Odd...")
assert isOdd(number) == False
print("False!")

number = 42
print(F"Testing if {number} is Even...")
assert isEven(number) == True
print("True!")

number = 9999
print(F"Testing if {number} is Even...")
assert isEven(number) == False
print("False!")

number = -10
print(F"Testing if {number} is Even...")
assert isEven(number) == True
print("True!")

number = -11
print(F"Testing if {number} is Even...")
assert isEven(number) == False
print("False!")

number = 3.1415
print(F"Testing if {number} is Even...")
assert isEven(number) == False
print("False!")
