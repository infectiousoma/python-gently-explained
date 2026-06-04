def isOdd(oddNumber):
  result = (oddNumber % 2) == 1
  return result

def isEven(evenNumber):
  result = (evenNumber % 2) == 0
  return result

while True:
  print("Provide any number")
  userInput = input()
  
  try:
    number = float(userInput)

  except ValueError:
    print("You must enter a number")
    continue

  if not number.is_integer():
      print(F"{number} isn't a whole number so it's neither even nor odd")
      continue

  number = int(number)
  if isOdd(number):
    print(F"{number} is odd")

  elif isEven(number):
    print(F"{number} is even")
  break