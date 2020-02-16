using System;
using System.IO;
using System.Threading;
using System.Threading.Tasks;

namespace getkey
{
  class Program
  {
    public static void Main (string[] args) {

      // Extract 0x1000 P values from Original.exe and Packed.exe.
      BinaryReader originalRdr = new BinaryReader(File.Open(@"C:\Users\r4k4\Documents\Wargame-Challenges\Reversing.Kr\PEPassword\Original.exe", FileMode.Open));
      BinaryReader packedRdr = new BinaryReader(File.Open(@"C:\Users\r4k4\Documents\Wargame-Challenges\Reversing.Kr\PEPassword\Packed.untouched.exe", FileMode.Open));
      byte[] originalTextArr = new byte[0x4000];
      byte[] packedTextArr = new byte[0x4000];
      originalRdr.BaseStream.Position = 0x1000;
      packedRdr.BaseStream.Position = 0x1000;
      originalRdr.Read(originalTextArr, 0x0, 0x4000);
      packedRdr.Read(packedTextArr, 0x0, 0x4000);
      uint[] p = new uint[0x1000];
      for(int i=0; i<0x1000; i++)
      {
        byte[] bytesFromOriginal = new byte[4];
        byte[] bytesFromPacked = new byte[4];
        Buffer.BlockCopy(originalTextArr, i * 4, bytesFromOriginal, 0, 4);
        Buffer.BlockCopy(packedTextArr, i * 4, bytesFromPacked, 0, 4);
        Array.Reverse(bytesFromOriginal);
        Array.Reverse(bytesFromPacked);
        uint uintFromOriginal = BitConverter.ToUInt32(bytesFromOriginal);
        uint uintFromPacked = BitConverter.ToUInt32(bytesFromPacked);
        p[i] = uintFromOriginal ^ uintFromPacked;
      }
      
      for (int i = 0x1000 - 1; i > 1; i--)
      {
        Console.WriteLine("p = 0x{0:X8} prev_p = 0x{1:X8}", p[i], p[i-1]);
        Parallel.For(0x0, 0xffffffff, (j) => {
          if (PrevP(p[i], (uint)j) == p[i-1]) {
            Console.WriteLine("q = 0x{0:X8} prev_q = 0x{1:X8}", (uint)j, PrevQ(p[i], (uint)j));
            if (NextQ(p[i-1], PrevQ(p[i], (uint)j)) == (uint)j) {
              Console.WriteLine("Gotcha!");
            }
          }
        });
      }
      /*
      for (int i = 0x1000 - 8; i < 0x1000 - 1; i++)
      {
        Console.WriteLine("p = 0x{0:X8} next_p = 0x{1:X8}", p[i], p[i+1]);
        Parallel.For(0x0, 0xffffffff, (j) => {
          if (NextP(p[i], (uint)j) == p[i+1]) {
            Console.WriteLine("q = 0x{0:X8} next_q = 0x{1:X8}", (uint)j, NextQ(p[i], (uint)j));
            if (PrevQ(p[i+1], NextQ(p[i], (uint)j)) == (uint)j) {
              Console.WriteLine("Gotcha!");
            }
          }
        });
      }
      */
    }

    public static uint NextP(uint p, uint q) {
      uint new_q = Rol(q, (int)l(p));
      uint new_p = p ^ new_q;
      new_p = Ror(new_p, (int)h(new_q));
      return new_p;
    }

    public static uint NextQ(uint p, uint q) {
      uint new_q = Rol(q, (int)l(p));
      uint new_p = p ^ new_q;
      new_p = Ror(new_p, (int)h(new_q));
      new_q = new_q + new_p;
      return new_q;
    }

    public static uint PrevP(uint p, uint q) {
      uint prev_q = q - p;
      uint prev_p = Rol(p, (int)h(prev_q));
      prev_p = prev_q ^ prev_p;
      prev_q = Ror(prev_q, (int)l(prev_p));
      return prev_p;
    }

    public static uint PrevQ(uint p, uint q) {
      uint prev_q = q - p;
      uint prev_p = Rol(p, (int)h(prev_q));
      prev_p = prev_q ^ prev_p;
      prev_q = Ror(prev_q, (int)l(prev_p));
      return prev_q;
    }

    public static uint l(uint data) {
      return data & 0x000000ff;
    }

    public static uint h(uint data) {
      return (data & 0x0000ff00) >> 8;
    }

    public static uint Rol(uint data, int shift, int size=32) {
      return (data << shift) | (data >> (size - shift));
    }

    public static uint Ror(uint data, int shift, int size=32) {
      return (data >> shift) | (data << (size - shift));
    }
  }
}