def fizzBuzz(upTo):
    for number in range(1, upTo + 1):
        if number % 15 == 0:
            print("FizzBuzz", end=' ')
        elif number % 3 == 0:
            print("Fizz", end=' ')
        elif number % 5 == 0:
            print("Buzz", end=' ')
        else:
            print(number, end=' ')

print("Enter a number to try to get FizzBuzz")
userInput = input ()
number = int(userInput)
fizzBuzz(number)