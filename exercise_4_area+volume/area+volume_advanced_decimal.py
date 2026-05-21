from decimal import Decimal, InvalidOperation

def area(length, width):
    result = (length * width)
    return result

def perimeter(length, width):
    result = (length * 2 + width * 2)
    return result

def volume(length, width, height):
    result = (length * width * height)
    return result

def surfaceArea(length, width, height):
    result = ((length * width) + (length * height) + (width * height)) * 2
    return result

while True:
    print("Please enter the length, width, and height of the object.")
    userInput = input()
    parts = userInput.split()

    if len(parts) != 3 :
        print("please enter each unit in the following order and format, length width height. Example 10 10 10")
        continue

    try:
        length = Decimal(parts[0])
        width = Decimal(parts[1])
        height = Decimal(parts[2])
        break

    except InvalidOperation:
        print("Values must be numbers")
        continue

print()
print(F"The area of your object is calculated with: lw | {length:g} * {width:g}")
print(f"The area is {area(length, width):g}")

print()
print(f"The perimeter of your object is calculated with: l+w+l+w | {length:g} + {width:g} + {length:g} + {width:g}")
print(f"The perimeter is {perimeter(length,width):g}")

print()
print(f"The volume of your object is calculated with: lwh | {length:g} * {width:g} * {height:g}")
print(f"The volume is is {volume(length, width, height):g}")

print()
print(
    f"The surface area of your object is calculated with: (2lw) + (2lh) + (2wh) | "
    f"(2 * {length:g} * {width:g}) + (2 * {length:g} *{height:g}) + (2 * {width:g} * {height:g})")
print(f"The surface area is {surfaceArea(length, width, height):g}")