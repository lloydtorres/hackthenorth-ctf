#!/usr/bin/python2

from subprocess import Popen, PIPE, STDOUT

success = "84c355da8831b62075d2ad9133ce6512"
firstSequence = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
secondSequence = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
thirdSequence = "abcdefghijklmnopqrstuvwxyz"

print "Working..."

def quickbash(sequence):
	for a1 in range(len(sequence)):
		p = Popen(['./securehash'], stdout=PIPE, stdin=PIPE, stderr=PIPE)
		stringbuilder = "yaaaaaaaaaaaaaa" + sequence[a1] + "aa"
		stdout_data = p.communicate(input=stringbuilder)[0].strip()
		if stdout_data[:2] == success[:2]:
			print "The missing letter is: '" + sequence[a1] + "'"

def fullbash():
	for a1 in range(32,127):
		p = Popen(['./securehash'], stdout=PIPE, stdin=PIPE, stderr=PIPE)
		stringbuilder = "yaaaaaaaaaaaaaa" + chr(a1) + "aa"
		stdout_data = p.communicate(input=stringbuilder)[0].strip()
		if stdout_data[:2] == success[:2]:
			print "The missing letter is: '" + chr(a1) + "'"

quickbash(thirdSequence)
quickbash(secondSequence)
quickbash(firstSequence)
fullbash()