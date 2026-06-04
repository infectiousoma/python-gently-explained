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

areaTests = [
    (10, 10, 100),
    (0, 9999, 0),
    (5, 8, 40)
]

for length, width, expected in areaTests:
    print(F"The area of an object with the length of {length} and width of {width} is {area(length, width)}")
    assert area(length, width) == expected
    print("Passed")

perimeterTests = [
    (10, 10, 40),
    (0, 9999, 19998),
    (5, 8, 26)
]

for length, width, expected in perimeterTests:
    print(F"The perimeter of an object with the length of {length} and width of {width} is {perimeter(length, width)}")
    assert perimeter(length, width) == expected
    print("Passed")

volumeTests = [
    (10, 10, 10, 1000   ),
    (9999, 0, 9999, 0),
    (5, 8, 10, 400)
]

for length, width, height, expected in volumeTests:
    print(F"The volume of an object with the length of {length} and width of {width} and height of {height} is {volume(length, width, height)}")
    assert volume(length, width, height) == expected
    print("Passed")

surfaceAreaTests = [
    (10, 10, 10, 600   ),
    (9999, 0, 9999, 199960002),
    (5, 8, 10, 340)
]

for length, width, height, expected in surfaceAreaTests:
    print(F"The surface area of an object with the length of {length} and width of {width} and height of {height} is {surfaceArea(length, width, height)}")
    assert surfaceArea(length, width, height) == expected
    print("Passed")
