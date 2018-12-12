#!/usr/bin/env python

file = open('input')

sum = 0

for line in file:
    if line[0] == "+":
        sum += int(line[1:])
    else:
        sum -= int(line[1:])

print sum
