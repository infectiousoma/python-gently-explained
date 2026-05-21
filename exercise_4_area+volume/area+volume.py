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

length = 10
width = 10
print(F"The area of an object with the length of {length} and width of {width} is {area(length, width)}")
assert area(10, 10) == 100
print("Passed")

length = 0
width = 9999
print(F"The area of an object with the length of {length} and width of {width} is {area(length, width)}")
assert area(0, 9999) == 0
print("Passed")

length = 5
width = 8
print(F"The area of an object with the length of {length} and width of {width} is {area(length, width)}")
assert area(5, 8) == 40
print("Passed")

length = 10
width = 10
print(F"The perimeter of an object with the length of {length} and width of {width} is {perimeter(length, width)}")
assert perimeter(10, 10) == 40
print("Passed")

length = 0
width = 9999
print(F"The perimeter of an object with the length of {length} and width of {width} is {perimeter(length, width)}")
assert perimeter(0, 9999) == 19998
print("Passed")

length = 5
width = 8
print(F"The perimeter of an object with the length of {length} and width of {width} is {perimeter(length, width)}")
assert perimeter(5, 8) == 26
print("Passed")

length = 10
width = 10
height = 10
print(F"The volume of an object with the length of {length} and width of {width} and height of {height} is {volume(length, width, height)}")
assert volume(10, 10, 10) == 1000
print("Passed")

length = 9999
width = 0
height = 9999
print(F"The volume of an object with the length of {length} and width of {width} and height of {height} is {volume(length, width, height)}")
assert volume(9999, 0, 9999) == 0
print("Passed")

length = 5
width = 8
height = 10
print(F"The volume of an object with the length of {length} and width of {width} and height of {height} is {volume(length, width, height)}")
assert volume(5, 8, 10) == 400
print("Passed")

length = 10
width = 10
height = 10
print(F"The surface area of an object with the length of {length} and width of {width} and height of {height} is {surfaceArea(length, width, height)}")
assert surfaceArea(10, 10, 10) == 600
print("Passed")

length = 9999
width = 0
height = 9999
print(F"The surface area of an object with the length of {length} and width of {width} and height of {height} is {surfaceArea(length, width, height)}")
assert surfaceArea(9999, 0, 9999) == 199960002
print("Passed")

length = 5
width = 8
height = 10
print(F"The surface area of an object with the length of {length} and width of {width} and height of {height} is {surfaceArea(length, width, height)}")
assert surfaceArea(5, 8, 10) == 340
print("Passed")
