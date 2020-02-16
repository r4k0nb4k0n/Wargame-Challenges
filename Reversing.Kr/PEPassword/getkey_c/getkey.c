#include <stdio.h>
#define DWORD unsigned long

DWORD toLittleEndian(DWORD dword)
{
  return (((dword >>  0) & 0xff) << 24)
        | (((dword >>  8) & 0xff) << 16)
        | (((dword >> 16) & 0xff) <<  8)
        | (((dword >> 24) & 0xff) <<  0);
}

DWORD l(DWORD data)
{
  return data & 0x000000ff;
}

DWORD h(DWORD data)
{
  return (data & 0x0000ff00) >> 8;
}

DWORD rol(DWORD data, int shift)
{
  int size = 32;
  return (data << shift) | (data >> (size - shift));
}

DWORD ror(DWORD data, int shift)
{
  int size = 32;
  return (data >> shift) | (data << (size - shift));
}

DWORD NextP(DWORD P, DWORD Q)  
{
  Q = rol(Q, (int)l(P));
  P = P ^ Q;
  P = ror(P, (int)h(Q));
  Q = Q + P;
  return P;
}  
  
DWORD NextQ(DWORD P, DWORD Q)  
{  
  Q = rol(Q, (int)l(P));
  P = P ^ Q;
  P = ror(P, (int)h(Q));
  Q = Q + P;
  return Q;
}

int main()
{
  DWORD originalTextArr[0x1000];
  DWORD packedTextArr[0x1000];
  DWORD p[0x1000];
  FILE *originalFp = fopen("..\\Original.exe", "rb");
  FILE *packedFp = fopen("..\\Packed.untouched.exe", "rb");
  fseek(originalFp, 0x1000, SEEK_SET);
  fseek(packedFp, 0x1000, SEEK_SET);
  for(int i=0; i<0x1000; i++) {
    DWORD dwordFromOriginal = 0x0;
    DWORD dwordFromPacked = 0x0;
    fread(&dwordFromOriginal, sizeof(DWORD), 1, originalFp);
    fread(&dwordFromPacked, sizeof(DWORD), 1, packedFp);
    dwordFromOriginal = toLittleEndian(dwordFromOriginal);
    dwordFromPacked = toLittleEndian(dwordFromPacked);
    p[i] = dwordFromOriginal ^ dwordFromPacked;
    p[i] = toLittleEndian(p[i]);
  }
  fclose(originalFp);
  fclose(packedFp);
  for(int i=0x0; i<0xD; i++) {
    printf("P = 0x%08X NextP = 0x%08X\n", p[i], p[i+1]);
    for(__int64 j=0; j<0xffffffff; j++) {
      if(NextP(p[i], (DWORD)j) == p[i+1]) {
        printf("Q = 0x%08X NextQ = 0x%08X\n", (DWORD)j, NextQ(p[i], (DWORD)j));
      }
    }
  }
  return 0;
}
