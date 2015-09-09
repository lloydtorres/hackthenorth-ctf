## hackthenorth-ctf

Hack the North held a CTF event from September 6-8, 2015 which consisted of hacking puzzles we needed to solve.

This repo contains some of the scripts I wrote to solve them.

### ./ssh-bruteforce/

This contains a Visual Studio .NET project that does a brute-force attack against the listed servers using a list of valid 
usernames and passwords. It then writes the valid ones it finds to a text file.

This was used to determine which accounts had access to the CTF servers we found.

### ./python-scripts/notecalc.py

This script takes in a list of MIDI notes (e.g. C#7, E7), converts them to their hex equivalent, then puts them sequentially into 
a target hash string with '`XX`' marking locations where these hex values can be put in.

This was used to solve the MIDI puzzle, where an incomplete hash was stored in a MIDI with some notes. Sadly, our MIDI-to-hex mapping 
was apparently different from the original, so this script produced the wrong hash.

### ./python-scripts/denigma.py

This script is related to the securehash puzzle. The script passes in a string consisting of one character repeated 18 times for 
each ASCII character into securehash. It then generates a mapping of how each ASCII character can be securehashed depending on its 
position in the original string. It then guesses the original string based on the provided hash. Due to the way securehash works, 
it can only "confidently" provide possible guesses for characters 3-14, since the other characters are obscured by securehash's 
unknown behaviour.

### ./python-scripts/oneletterguesser.py

This script is used to identify the 15th character of the original string based on the behaviour of securehash and the clues given 
to us. This script was used to raise the brute force script's efficiency from O(n^5) to O(n^4) (which brought down the number of 
possibilities to test from 370 billion to just 4 billion).

### ./python-scripts/brutehash.py

Based on the information found through denigma and oneletterguesser, this script brute-forces through 4 billion possible combinations 
to determine the original string from the given hash. It first goes through alphanumeric ASCII; if that fails, it goes on to the full set. 
It took about an hour for this script to find the original string.

### ./python-scripts/securehash

This was the securehash program provided during the CTF. This is not by me, but my scripts rely on it.