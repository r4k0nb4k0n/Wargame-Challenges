using System;
using System.Text;
namespace HelloWorld
{
    class Hello 
    {
        static void Main() 
        {
			string name = "CodeEngn";
			ytrewq ytrewq = new ytrewq();
			uint num = Convert.ToUInt32("28BF522F", 16);
			uint num2 = Convert.ToUInt32("A5BE61D1", 16);
			uint num4 = ytrewq.qwerty(dfgsf(name));
			uint hashCode = (uint)name.GetHashCode();
			uint[] ewrrr = new uint[6];
			ewrrr[0] = 1082200817u;
			ewrrr[1] = 440077137u;
			ewrrr[2] = 693619197u;
			ewrrr[3] = 456293661u;
			ewrrr[4] = 2743929585u;
			ewrrr[5] = 718661953u;
			Console.WriteLine(String.Format("Brute force with {0:X8}, {1:X8} and {2:X8}...", num, num2, hashCode));
			for(uint token3 = 0u; token3 <= UInt32.MaxValue; token3+=1u){
				if(token3 % 99999999u == 0){
					String done = String.Format("Please.... 0x{0:X8} done...", token3);
					Console.WriteLine(done);
				}
				uint num3 = token3;
				num3 ^= hashCode;
				uint[] yreee = new uint[4];
				yreee[0] = num;
				yreee[1] = num2;
				yreee[2] = num;
				yreee[3] = num2;
				bool flag = vxzzz(yreee, ewrrr, 2415796773u, num3);
				if (flag && yreee[2] == hashCode && yreee[3] == num4)
				{
					String gotit = String.Format("Congratulation! Broke this shit!!!! 0x{0:X8}", token3);
					Console.WriteLine(gotit);
					break;
				}
			}
        }
		
		public static byte[] dfgsf(string str)
		{
			ASCIIEncoding asciiencoding = new ASCIIEncoding();
			return asciiencoding.GetBytes(str);
		}
		
		static bool vxzzz(uint[] rwerqw, uint[] kgtsdfs, uint pgdsfa, uint fsfsdf)
		{
			pgdsfa ^= fsfsdf;
			uint num = pgdsfa % 57u - 1u;
			uint num2 = rwerqw[0];
			uint num3 = rwerqw[1];
			uint num4 = num;
			uint num5 = pgdsfa << (int)((byte)(97u ^ num + 68u));
			if (num <= 0u || num >= 56u)
			{
				return false;
			}
			while (num-- > 0u)
			{
				uint num6 = num4 / 16u;
				uint num7 = num2 << (int)((byte)(num4 / 8u));
				uint num8 = num2 >> (int)(3 + (byte)num6);
				uint num9 = num4 / 4u + 3u;
				uint num10 = num9;
				num9 = kgtsdfs[(int)((UIntPtr)((num5 >> (int)((byte)num9)) % 4u))];
				uint num11 = num5 + num9;
				num3 -= ((num7 ^ num8) + num2 ^ num11) - num;
				num5 -= pgdsfa;
				num3 -= num;
				num7 = num3 << (int)((byte)(num10 + 1u) ^ 8);
				num8 = num3 >> (int)((byte)(num4 / 2u - num10 + 23u) ^ 25);
				if (num == num4)
				{
					num3 ^= num;
				}
				if (num == num4 / 2u + (num10 ^ 27u))
				{
					num10 = (num7 ^ num8) + (num3 ^ num);
				}
				else
				{
					num10 = (num7 ^ num8) + num3;
				}
				num2 -= (num10 ^ num5 + kgtsdfs[(int)((UIntPtr)(num5 & 3u))]);
			}
			rwerqw[0] = (num2 ^ 4u);
			rwerqw[1] = (num3 ^ 7u);
			rwerqw[2] = (rwerqw[1] ^ (uint)((byte)((num4 + 1u) / 3u - 4u)));
			rwerqw[3] = (rwerqw[0] ^ (uint)((byte)(num4 - 21u + 1u ^ 8u)));
			rwerqw[0] = (rwerqw[0] ^ kgtsdfs[4]);
			rwerqw[1] = (rwerqw[1] ^ kgtsdfs[5]);
			return true;
		}
    }
	
	public class ytrewq
	{
		// Token: 0x0600000D RID: 13 RVA: 0x000027C8 File Offset: 0x000009C8
		public uint qwerty(byte[] bytes)
		{
			uint num = 0u;
			num = ~num;
			for (int i = 0; i < bytes.Length; i++)
			{
				byte b = (byte)((num & 255u) ^ (uint)bytes[i]);
				num = (num >> 8 ^ this.tqepq[(int)b]);
			}
			return ~num;
		}

		// Token: 0x0600000E RID: 14 RVA: 0x00002804 File Offset: 0x00000A04
		public ytrewq()
		{
			uint num = 3131961357u;
			this.tqepq = new uint[256];
			uint num2 = 0u;
			while ((ulong)num2 < (ulong)((long)this.tqepq.Length))
			{
				uint num3 = num2;
				for (int i = 8; i > 0; i--)
				{
					if ((num3 & 1u) == 1u)
					{
						num3 = (num3 >> 1 ^ num);
					}
					else
					{
						num3 >>= (int)((byte)(num / num));
					}
				}
				this.tqepq[(int)((UIntPtr)num2)] = num3;
				num2 += 1u;
			}
		}

		// Token: 0x0400000B RID: 11
		private uint[] tqepq;
	}
}

/*
28BF522F-A5BE61D1-XXXXXXXX
*/