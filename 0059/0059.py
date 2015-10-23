import time

start_time = time.time()

# Import the words from the text file
with open("./cipher.txt","r") as f:
    cipher = [int(s) for s in f.read().split(',')]

cipher_length = len(cipher)
characters = range(ord('a'), ord('z')+1)

string = ""

for key in [[a, b, c] for a in characters for b in characters for c in characters]:
	string = ""
	for i in range(cipher_length):
		string += chr( cipher[i] ^ key[i % 3] )
	if(' and ' in string) and (' the ' in string) and (' a ' in string) :
		print string
		print sum([int(ord(char)) for char in string])
		break


print "Finished in ", time.time() - start_time, "seconds"