# --- Day 2 ---
import numpy as np
"""
A: Rock
B: Paper
C: Scissors
 
A < B < C < A

X: Rock
Y: Paper
Z: Scissors 

X < Y < Z < X

Rock: 1pt, Paper: 2pt, Scissors: 3pt
"""

points = {}
points['X'] = 0
points['Y'] = 3
points['Z'] = 6

symX = np.array(['X','Y','Z'])
symA = np.array(['A','B','C'])

total = 0

in_file = open("02_input.txt",'r')
lines = in_file.readlines()

for line in lines:
    a_line = line.replace("\n","").split(" ")

    # add symbol point
    total += points[a_line[1]]

    # win, draw, or lose
    sym = symA[np.where(symX==a_line[1])]

    if a_line[0] == sym: # draw
        total += 3
    elif (a_line[0] == 'A' and sym == 'B') or (a_line[0] == 'B' and sym == 'C') or (a_line[0] == 'C' and sym == 'A'):
        total += 6

print(total)