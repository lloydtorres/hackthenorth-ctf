#!/usr/bin/python2

from subprocess import Popen, PIPE, STDOUT

chars = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~ "
sequences = []
for i in range(15):
	sequences.append([])

for i in range(len(chars)):
	p = Popen(['./securehash'], stdout=PIPE, stdin=PIPE, stderr=PIPE)
	builder = chars[i] * 18
	stdout_data = p.communicate(input=builder)[0].strip()
	stdout_data = stdout_data[:30]

	for j in range(len(stdout_data)/2):
		hexHold = stdout_data[j*2:j*2+2]
		sequences[j].append(hexHold)


target = "84c355da8831b62075d2ad9133ce65"

password = ""

for s in range(len(sequences)):
	print "Sequence " + str(s)
	print sequences[s]
	print "==="

for i in range(3,len(target)/2):
    hexHold = target[i*2:i*2+2]
    if hexHold in sequences[i]:
    	print chars[sequences[i].index(hexHold)]+ " " + hexHold + ", index: " + str(sequences[i].index(hexHold))
    	password += chars[sequences[i].index(hexHold)]
    else:
		password += "?"
    print password