#GROUP ASSIGNMENT
#NAME: HINA ALI BHATTI      ROLL No.: BSEF20M009
#NAME: NOREEN               ROLL No.: BSEF20M036


# Python3 program for the above approach
# of RC4 algorithm

# Function for encryption
def encryption():
    global key, plain_text, n
    plain_text = input("Enter Plain Text in Binary Form: ")
	key = input("Enter Key in Binary Form: ")
	# n is the number of bits to be considered at a time to convert it to decimal
	n = 3
	print("Your Plain text in DECIMAL: ", plain_text)
	print("Your Key in DECIMAL: ", key)
	#print("n : ", n)
	print(" ")
	# The initial state vector array
	S = [i for i in range(0, 2**n)]
	print("S : ", S)
	key_list = [key[i:i + n] for i in range(0, len(key), n)]
	# Convert to key_stream to decimal
	for i in range(len(key_list)):
		key_list[i] = int(key_list[i], 2)
	# Convert to plain_text to decimal
	global pt0
	pt = [plain_text[i:i + n] for i in range(0, len(plain_text), n)]
	for i in range(len(pt)):
		pt[i] = int(pt[i], 2)
	print("Plain text ( in array form ): ", pt)
	# Making key_stream equal
	# to length of state vector
	diff = int(len(S)-len(key_list))
	if diff != 0:
		for i in range(0, diff):
			key_list.append(key_list[i])
	print("Key list : ", key_list)
	print(" ")

	# Perform the KSA algorithm
def KSA():
	j = 0
	N = len(S)
		
	# Iterate over the range [0, N]
	for i in range(0, N):
		# Find the key
		j = (j + S[i]+key_list[i]) % N
			
			# Update S[i] and S[j]
		S[i], S[j] = S[j], S[i]
		print(i, " ", end ="")
			
			# Print S
		print(S)

		initial_permutation_array = S
		
		print(" ")
		print("The initial permutation array is : ",
			initial_permutation_array)

print("KSA iterations : ")
print(" ")
KSA()
print(" ")

	# Perform PGRA algorithm
	def PGRA():

		N = len(S)
		i = j = 0
		global key_stream
		key_stream = []

		# Iterate over [0, length of pt]
		for k in range(0, len(pt)):
			i = (i + 1) % N
			j = (j + S[i]) % N
			
			# Update S[i] and S[j]
			S[i], S[j] = S[j], S[i]
			print(k, " ", end ="")
			print(S)
			t = (S[i]+S[j]) % N
			key_stream.append(S[t])

		# Print the key stream
		print("Key stream : ", key_stream)
		print(" ")

	print("RC4 iterations : ")
	print(" ")
	PGRA()

	# Performing XOR between generated
	# key stream and plain text
	def XOR():
		global cipher_text
		cipher_text = []
		for i in range(len(pt)):
			c = key_stream[i] ^ pt[i]
			cipher_text.append(c)

	XOR()

	# Convert the encrypted text to
	# bits form
	encrypted_to_bits = ""
	for i in cipher_text:
		encrypted_to_bits += '0'*(n-len(bin(i)[2:]))+bin(i)[2:]

	print(" ")
	print("Cipher text : ", encrypted_to_bits)


encryption()

print("---------------------------------------------------------")

# Function for decryption of data
def decryption():

	# The initial state vector array
	S = [i for i in range(0, 2**n)]

	key_list = [key[i:i + n] for i in range(0, len(key), n)]

	# Convert to key_stream to decimal
	for i in range(len(key_list)):
		key_list[i] = int(key_list[i], 2)

	# Convert to plain_text to decimal
	global pt

	pt = [plain_text[i:i + n] for i in range(0, len(plain_text), n)]

	for i in range(len(pt)):
		pt[i] = int(pt[i], 2)

	# making key_stream equal
	# to length of state vector
	diff = int(len(S)-len(key_list))

	if diff != 0:
		for i in range(0, diff):
			key_list.append(key_list[i])

	print(" ")

	# KEY STREAM  Algorithm
	def KSA():
		j = 0
		N = len(S)
		
		# Iterate over the range [0, N]
		for i in range(0, N):
			j = (j + S[i]+key_list[i]) % N
			
			# Update S[i] and S[j]
			S[i], S[j] = S[j], S[i]
			print(i, " ", end ="")
			print(S)

		initial_permutation_array = S
		print(" ")
		print("The initial permutation array is : ",
			initial_permutation_array)

	print("KSA iterations : ")
	print(" ")
	KSA()
	print(" ")

	# Perform RC4 algorithm
def do_RC4():

		N = len(S)
		i = j = 0
		global key_stream
		key_stream = []

		# Iterate over the range
		for k in range(0, len(pt)):
			i = (i + 1) % N
			j = (j + S[i]) % N
			
			# Update S[i] and S[j]
			S[i], S[j] = S[j], S[i]
			print(k, " ", end ="")
			print(S)
			t = (S[i]+S[j]) % N
			key_stream.append(S[t])

	print("Key stream : ", key_stream)
	print(" ")

	print("RC4 iterations : ")
	print(" ")
	do_RC4()

	# Perform XOR between generated
	# key stream and cipher text
def do_XOR():
	global original_text
	original_text = []
	for i in range(len(cipher_text)):
		p = key_stream[i] ^ cipher_text[i]
		original_text.append(p)
    print("CIPHER IN  DECIMAL FORM: ", original_text)


do_XOR()

# convert the decrypted text to
# the bits form
decrypted_to_bits = ""
for i in original_text:
	decrypted_to_bits += '0'*(n-len(bin(i)[2:]))+bin(i)[2:]
print("----------------------------------------------------------------")
print("Decrypted text : ", decrypted_to_bits)

# Driver Code
decryption()
