# Open files
file_encrypted = open("encrypted", "rb")
file_key = open("key", "rb")

# Read bytes and close file descriptor
encrypted = file_encrypted.read()
key_unfiltered = file_key.read()
file_encrypted.close()
file_key.close()

# Get only key bytes
key = [key_unfiltered[i] for i in range(0, len(key_unfiltered)+1, 0x210)]

# Decode
l = len(key)
decrypted = "".join([chr(encrypted[i]^key[i]) for i in range(l)])

# Print
print(decrypted)