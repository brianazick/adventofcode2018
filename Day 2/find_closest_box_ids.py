#!/usr/bin/env python

input_file = open('input.txt', 'r')

input_words = dict()
line_counter = 0

for line in input_file:
    input_words[line_counter] = line.strip()
    line_counter += 1

closest_pair = ('','')
correct_common_letters = ''
min_distance = len(input_words[0])

for key1 in input_words:
    for key2 in input_words:
        distance = 0
        common_letters = ''

        str1 = input_words[key1]
        str2 = input_words[key2]

        for index in range(len(str1)):
            if str1[index] != str2[index]:
                distance += 1
            else:
                common_letters += str1[index]

        if distance < min_distance and key1 != key2:
            closest_pair = (str1, str2)
            min_distance = distance
            correct_common_letters = common_letters

print closest_pair
print min_distance
print correct_common_letters
