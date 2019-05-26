from itertools import cycle

key = bytes([0x10, 0x20, 0x30])

serial = input('Enter the input Serial => ')
serial_bytes = bytes.fromhex(serial).decode().encode('ascii')

name = bytes([a ^ b for a, b in zip(serial_bytes, cycle(key))])
name = name.decode('ascii')

print(name, 'is generated from', serial)