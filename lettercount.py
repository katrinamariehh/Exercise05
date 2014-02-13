from sys import argv

script, filename = argv

f = open(filename)
letters = f.read()
f.close()

letters = letters.lower()

alphabet = [0] * 26

for letter in letters:
    # if the character is not between a and z, pass
    if not ord(letter) >= ord('a') and ord(letter) <= ord('z'):
        pass
    else:
    # if the character is between a and z, add 1 to that position in that alphabet list
        index = ord(letter) - 97
        alphabet[index] += 1

for i in range (len(alphabet)):
    print chr(i + 97), 
    print alphabet[i]