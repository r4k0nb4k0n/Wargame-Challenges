using System;
using System.Threading;
using System.Threading.Tasks;

class Program
{
  public static void Main (string[] args) {
    UInt32[] lastP = new UInt32[4]{0x2be16e72, 0x5a08c120, 0xad5b56ca, 0x07b3a312};
    for (int i = 0; i < 3; i++)
    {
      Console.WriteLine("{0:X8}", lastP[i]);
      Parallel.For(0x0, 0xffffffff + 1, (j) => {
        if (NextP(lastP[i], j) == lastP[i+1]) {
          Console.WriteLine("q = {0:X8} next_q = {1:X8}", j, next_q(lastP[i], j));
        }
      });
    }
  }

  public UInt32 NextP(UInt32 p, UInt32 q) {
    q = Rol(q, p & 0x000000ff);
    p = p ^ q;
    p = Ror(p, (q & 0x0000ff00) >> 8);
    return p;
  }

  public UInt32 NextQ(UInt32 p, UInt32 q) {
    q = Rol(q, p & 0x000000ff);
    p = p ^ q;
    p = Ror(p, (q & 0x0000ff00) >> 8);
    q = q + p;
    return q;
  }

  public UInt32 Rol(UInt32 data, UInt32 shift, UInt32 size=32) {
    shift %= size;
    UInt32 remains = data >> (size - shift);
    UInt32 body = (data << shift) - (remains << size);
    return body + remains;
  }

  public UInt32 Ror(UInt32 data, UInt32 shift, UInt32 size=32) {
    shift %= size;
    UInt32 body = data >> shift;
    UInt32 remains = (data << (size - shift)) - (body << size);
    return body + remains;
  }
}