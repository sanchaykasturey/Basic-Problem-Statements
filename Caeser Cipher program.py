def encryption_cc(befroreEncryption, keyEncryption):
	encrypted = []
	process = []

	uppercase = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
	lowercase = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

	for eachLetter in befroreEncryption:
		if eachLetter in uppercase:
			index = uppercase.index(eachLetter)
			crypting = (index + keyEncryption) % 26
			process.append(crypting)
			newLetter = uppercase[crypting]
			encrypted.append(newLetter)
		elif eachLetter in lowercase:
			index = lowercase.index(eachLetter)
			crypting = (index + keyEncryption) % 26
			process.append(crypting)
			newLetter = lowercase[crypting]
			encrypted.append(newLetter)
	return encrypted

befroreEncryption = str(input("Enter the message"))
keyEncryption = int(input("Enter the key"))
print()
print(encryption_cc(befroreEncryption, keyEncryption))
print()
