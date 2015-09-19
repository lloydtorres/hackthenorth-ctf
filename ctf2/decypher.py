#!/usr/bin/python2

import numpy

psk = [3,1,4,8,23,21,12,22,19,16,10,18,15,24,14,5,25,9,6,11,26,7,13,17,2,20]
ciphertext = "ZEBRVJWBMQHOIVWNUTKNOGGWPQ"
aorigin = (8,15)
basis = [(3,1),(-2,1)]
vectors = [(2,1),(2,3),(4,6),(0,-2),(0,-1),(5,7),(4,8),(5,2),(2,-3)]

# Parse through the encrypted grid's rows
inFile = open("grid1to26","r")
rows = inFile.readlines()
inFile.close()

grid = []
for r in rows:
    x = r.strip().split()
    grid.append(x)

# Convert the columns into its own list
colgrid = []

for i in range(26):
    tmpGrid = []
    for j in range(26):
        tmpGrid.append(grid[j][i])
    colgrid.append(tmpGrid)

# Shift each column so that the first row reads the ciphertext
cgrid = []

for p in range(len(psk)):
    holder = "".join(colgrid[psk[p]-1])
    ti = holder.index(ciphertext[p])
    holder = holder[ti:] + holder[:ti]
    cgrid.append(list(holder))

# Rotate the grid back
newgrid = []

for i in range(26):
    tmpGrid = []
    for j in range(26):
        tmpGrid.append(cgrid[j][i])
    newgrid.append(tmpGrid)

# Print the results
for n in newgrid:
    print " ".join(n)

print "==="

# Find password

password = ""

for v in vectors:
    # Change basis of each vector from standard
    newvector = numpy.rint(numpy.dot(v, basis))
    password = password + newgrid[aorigin[1] - int(newvector[1]) - 1][aorigin[0] + int(newvector[0]) - 1]

print password
