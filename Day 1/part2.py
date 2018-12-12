#!/usr/bin/env python

inputfile = open('input')

inputvalues = []

for line in inputfile:
    inputvalues.append(line)

for x in range(10):
    inputvalues = inputvalues + inputvalues

sum = 0
listofsums = []
repeatfound = False

for line in inputvalues:
    if line[0] == "+":
        sum += int(line[1:])
    else:
        sum -= int(line[1:])

    for value in listofsums:
        if value == sum:
            repeatfound = True
            print "Repeat found: " + str(sum)
    listofsums.append(sum)

print "Sum is " + str(sum)
