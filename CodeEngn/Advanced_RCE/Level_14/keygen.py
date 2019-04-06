name = input('name> ')
key = 'NH6-0-'
base = 'NH KeyGenMe6'

if len(name) != 0xC:
	print('Name is not 13 characters...')
else:
	for i in range(3):
		key += ('00' + hex(ord(name[i]) + ord(base[i]))[2:].upper())

print(key)
