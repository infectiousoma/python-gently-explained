def convertToFahrenheit(degreesCelsius):
  result = (degreesCelsius * (9 / 5) + 32)
  return result
def convertToCelsius(degreesFahrenheit):
  result = (degreesFahrenheit - 32) * (5 / 9)
  return result

number = 0
print(F"Testing if {number} F is equal to -17.77777777777778 C")
assert convertToCelsius(number) == -17.77777777777778
print("Passed!")

number = 180
print(F"Testing if {number} F is equal to 82.22222222222223 C")
assert convertToCelsius(number) == 82.22222222222223
print("Passed!")

number = 0
print(F"Testing if {number} C is equal to 32 F")
assert convertToFahrenheit(number) == 32
print("Passed!")

number = 100
print(F"Testing if {number} C is equal to 212 F")
assert convertToFahrenheit(100) == 212
print("Passed!")

number = 15
print(F"Testing converting {number} C to fahrenheit then back to celsius is {number} C")
assert convertToCelsius(convertToFahrenheit(number)) == 15
print("Passed!")
