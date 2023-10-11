#!/usr/bin/python3
def roman_to_int(roman_string):
    if not isinstance(roman_string, str) or roman_string is None:
        return 0

    roman_numerals = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000,
    }

    sum = 0
    prev_value = 0

    for letter in reversed(roman_string):
        value = roman_numerals[letter]

        if value >= prev_value:
            sum += value  # Add the current value if it's greater or equal to the previous value
        else:
            sum -= value  # Subtract the current value if it's less than the previous value

        prev_value = value

    return sum
