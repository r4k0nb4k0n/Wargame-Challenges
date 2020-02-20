operand = 26729
c = -1536092243306511225

k = 0
while True:
  if (k * 2**64 + c) % operand == 0:
    print("k = %d" % k)
    break
  k += 1

not_overflowed_value = (k * 2**64 + c) // operand

if not_overflowed_value > 0x7fffffffffffffff:
  overflowed_value = not_overflowed_value - 2**64
  print("target = %d" % overflowed_value)
else:
  print("target = %d" % not_overflowed_value)
