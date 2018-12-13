#!/usr/bin/env python

input_file = open('input.txt', 'r')

num_ids_letter_twice = 0
num_ids_letter_thrice = 0

for line in input_file:
    line = line.strip()
    char_occurences = dict()
    twice_counted_for = False
    thrice_counted_for = False

    for char in line:
        print char
        if char not in char_occurences:
            char_occurences[char] = 1
        else:
            char_occurences[char] += 1

    for key in char_occurences:
        if char_occurences[key] == 2 and not twice_counted_for:
            num_ids_letter_twice += 1
            twice_counted_for = True
        elif char_occurences[key] == 3 and not thrice_counted_for:
            num_ids_letter_thrice += 1
            thrice_counted_for = True
    print char_occurences

checksum = num_ids_letter_twice * num_ids_letter_thrice
print num_ids_letter_twice
print num_ids_letter_thrice
print checksum
