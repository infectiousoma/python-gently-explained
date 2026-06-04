def ordinalSuffix(number):
    numberStr = str(number)

    # 11, 12, and 13 have the suffix th:
    if numberStr[-2:] in ['11', '12', '13']:
        return numberStr + 'th'

    # Numbers that end with 1 have the suffix st:
    if numberStr[-1] == '1':
        return numberStr  + 'st'

    # Numbers that end with 2 have the suffix nd:
    if numberStr[-1] == '2':
        return numberStr + 'nd'

    # Numbers that end with 3 have the suffix rd:
    if numberStr[-1] == '3':
        return numberStr + 'rd'

    # All other numbers end with th:
    return numberStr + 'th'

assert ordinalSuffix(0) == '0th'

assert ordinalSuffix(1) == '1st'

assert ordinalSuffix(2) == '2nd'

assert ordinalSuffix(3) == '3rd'

assert ordinalSuffix(4) == '4th'

assert ordinalSuffix(10) == '10th'

assert ordinalSuffix(11) == '11th'

assert ordinalSuffix(12) == '12th'

assert ordinalSuffix(13) == '13th'

assert ordinalSuffix(14) == '14th'

assert ordinalSuffix(101) == '101st'
