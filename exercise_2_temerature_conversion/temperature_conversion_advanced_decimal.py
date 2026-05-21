from decimal import Decimal, InvalidOperation

def convertToFahrenheit(degreesCelsius):
    result = (degreesCelsius * (Decimal(9) / Decimal(5)) + Decimal(32))
    return result


def convertToCelsius(degreesFahrenheit):
    result = (degreesFahrenheit - Decimal(32)) * (Decimal(5) / Decimal(9))
    return result

while True:
  print("Provide a temperature in Celsius or Fahrenheit which you want to convert")
  userInput = input()
  parts = userInput.split()

  if len(parts) !=2:
    print("Enter a temperature and unit, like: 100 C")
    continue

  try:
    temperature = Decimal(parts[0])

  except InvalidOperation:
    print("Temperature must be a number")
    continue

  unit = str(parts[1].upper())
  if unit != "C" and unit != "F":
    print("You must enter C or F")
    continue
    
  if unit == 'C':
    value = convertToFahrenheit(temperature)
    print(f"{float(value):g}")
  
  elif unit == 'F':
    value = convertToCelsius(temperature)
    print(f"{float(value):g}")
  
  else:
      print("Invalid unit")
      continue
  break
