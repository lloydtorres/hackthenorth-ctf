#!/usr/bin/python2

notes = ['C#7', 'F#6', 'F#7', 'C#4', 'B7', 'C7', 'D#7', 'E7', 'F#7', 'F#7', 'D#5', 'G#7', 'F7', 'F#5', 'E7', 'A#2', 'G7', 'D5', 'G5', 'F#7', 'B7', 'E4', 'D6', 'D5', 'E7', 'D5', 'F4', 'C#3']
target = "80XXXXXXbe7bXXXXe7d2e2XXXXa18678XX76c2f9XXXX05d78ebda4XXXXf6XXXXXXXX74bac0d19bXXabXXXX990b7de2XXXX97c9c2XXf8XXXXc4XXdfXXXXXX4"

baseNotes = {"C":0, "C#":1, "D":2, "D#":3, "E":4, "F":5, "F#":6, "G":7, "G#":8, "A":9, "A#":10, "B":11}

for n in notes:
    letter = n[:-1]
    octave = int(n[-1])
    value = baseNotes[letter] + octave * 12
    print n + " " + str(value)
    toReplace = target.index("XX")
    target = target[:toReplace] + hex(value)[-2:] + target[toReplace+2:]

print target
