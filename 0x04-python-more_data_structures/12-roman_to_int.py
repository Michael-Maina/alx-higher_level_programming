#!/usr/bin/python3
def roman_to_int(roman_string):
    if not isinstance(roman_string, str) or roman_string is None:
        return 0
    total = 0
    prev_val = 0
    ref = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    for i in range(len(roman_string)):
        if prev_val < ref[roman_string[i]]:
            total -= prev_val * 2
        total += ref[roman_string[i]]
        prev_val = ref[roman_string[i]]
    return total
