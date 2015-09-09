#!/usr/bin/python2

from subprocess import Popen, PIPE, STDOUT

success = "84c355da8831b62075d2ad9133ce6512"
firstSequence = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

s0 = ["s", "$"]
s1 = ["e", "t", "G", "V"]
s2 = ["x", ">", "["]
s3 = ["1", "p"]

noHashes = 0

print "Working..."

def quickbash(sequence):
	for a1 in range(len(sequence)):
		for a2 in range(len(sequence)):
			for a4 in range(len(sequence)):
				for a5 in range(len(sequence)):
					for b in s1:
						for c in s2:
							for d in s3:
								for s in s0:
									p = Popen(['./securehash'], stdout=PIPE, stdin=PIPE, stderr=PIPE)
									stringbuilder = "y" + sequence[a1] + sequence[a2] + "a" + s + "ecurity" + b + c + d + "U" + sequence[a4] + sequence[a5]
									stdout_data = p.communicate(input=stringbuilder)[0].strip()
									if stdout_data == success:
										print "PASSWORD: '" + stringbuilder + "'"
										inFile = open("./PASSWORD.txt", "w")
										inFile.write(stringbuilder)
										inFile.close()
										return True
	return False

def fullbash():
	for a1 in range(32,127):
		for a2 in range(32,127):
			for a4 in range(32,127):
				for a5 in range(32,127):
					for b in s1:
						for c in s2:
							for d in s3:
								for s in s0:
									p = Popen(['./securehash'], stdout=PIPE, stdin=PIPE, stderr=PIPE)
									stringbuilder = "y" + chr(a1) + chr(a2) + "a" + s + "ecurity" + b + c + d + "U" + chr(a4) + chr(a5)
									stdout_data = p.communicate(input=stringbuilder)[0].strip()
									if stdout_data == success:
										print "PASSWORD: '" + stringbuilder + "'"
										inFile = open("./PASSWORD.txt", "w")
										inFile.write(stringbuilder)
										inFile.close()
										return

flag = quickbash(firstSequence)
if not flag:
	print "Quick bash finished. Password was not found."
	fullbash()