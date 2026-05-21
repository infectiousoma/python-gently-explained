def convertToFahrenheit(degreesCelsius):
    result = (degreesCelsius * (9 / 5) + 32)
    return result


def convertToCelsius(degreesFahrenheit):
    result = (degreesFahrenheit - 32) * (5 / 9)
    return result

while True:
  print("Provide a temperature in Celsius or Fahrenheit which you want to convert")
  userInput = input()
  parts = userInput.split()

  if len(parts) !=2:
    print("Enter a temperature and unit, like: 100 C")
    continue

  try:
    temperature = float(parts[0])

    
  except ValueError:
    print("Temperature must be a number")

  unit = str(parts[1].upper())
  if unit != "C" and unit != "F":
    print("You must enter C or F")
  
  if unit == 'C':
    value = convertToFahrenheit(temperature)
    print(f"{value:g}")
  
  elif unit == 'F':
    value = convertToCelsius(temperature)
    print(f"{value:g}")
    
  else:
      print("Invalid unit")
      continue
  break