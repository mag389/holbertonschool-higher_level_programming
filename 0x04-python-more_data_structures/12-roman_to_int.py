#!/usr/bin/python3
def roman_to_int(roman_string):
    if not roman_string or not isinstance(roman_string, str):
        return 0
    nums = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    num = 0
    for i in range(0, len(roman_string) - 1):
        if nums[roman_string[i]] < nums[roman_string[i + 1]]:
            num -= nums[roman_string[i]]
        else:
            num += nums[roman_string[i]]
    return num + nums[roman_string[-1]]
