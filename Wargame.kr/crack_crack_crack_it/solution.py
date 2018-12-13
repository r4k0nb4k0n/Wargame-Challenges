from itertools import combinations, product
import sys, crypt

symbols = "abcdefghijklmnopqrstuvwxyz"+"0123456789"
max_length = len(symbols)

head = 'G4HeulB'

for length in range(1, 6 + 1):
    for word in product(symbols, repeat=length):
        print head + ''.join(word)
