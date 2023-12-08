#!/usr/bin/python3
def roman_to_int(roman_numeral):
    if not roman_numeral or type(roman_numeral) != str:
        return 0
    roman_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    result = 0
    prev_value = 0
    for i in range(len(roman_numeral)):
        current_value = roman_dict[roman_numeral[i]]
        if i > 0 and current_value > prev_value:
            result += current_value - 2 * prev_value
        else:
            result += current_value
        prev_value = current_value
    return result
