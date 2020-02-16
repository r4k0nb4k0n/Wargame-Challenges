"""
* `q' = q rol p[0]`
* `p' = p ^ q'`
* `p'' = p' ror q'[1] = (p ^ q') ror q'[1]`
* `q'' = p'' + q'`
"""

"""
p_last = 0x07B3A312
q_last = 0x07B3A312 + (q_last-1 rol 0xCA)
p_last-1 =  0xAD5B56CA
q_last-1 = 0x????????
p_last-2 = 0x5A08C120
q_last-2 = 
p_last-3 = 0x2BE16E72
q_last-3 = 
"""

"""
0x2be16e72
q =  0x49992a74 next_q =  0x2be16e72
q =  0xd78e8f58 next_q =  0x2be16e72
0x5a08c120
q =  0xf621b96 next_q =  0x5a08c122
q =  0x36a21495 next_q =  0x5a08c122
"""

original_text = None
packed_text = None

with open("Original.exe", "rb") as f:
  original_text = f.read()
  original_text = original_text[1000:5000]

with open("Packed.exe", "rb") as f:
  packed_text = f.read()
  packed_text = original_text[1000:5000]

last_p = [0x2be16e72, 0x5a08c120, 0xad5b56ca, 0x07b3a312]

def rol(data, shift, size=32):
  shift %= size
  remains = data >> (size - shift)
  body = (data << shift) - (remains << size )
  return (body + remains)
     
 
def ror(data, shift, size=32):
  shift %= size
  body = data >> shift
  remains = (data << (size - shift)) - (body << size)
  return (body + remains)

def next_p(p, q):
  q = rol(q, p & 0x000000ff)
  p = p ^ q
  p = ror(p, (q & 0x0000ff00) >> 8)
  return p

def next_q(p, q):
  q = rol(q, p & 0x000000ff)
  p = p ^ q
  p = ror(p, (q & 0x0000ff00) >> 8)
  q = q + p
  return q

for i in range(3):
  print(hex(last_p[i]))
  for j in range(0x0, 0xffffffff + 1):
    if next_p(last_p[i], j) == last_p[i+1]:
      print("q = ", hex(j), "next_q = ", hex(next_q(last_p[i], i)))
