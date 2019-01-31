#include <cstdio>

typedef unsigned int ui;

ui generate_first_token(ui seed)
{
	ui c = seed;
	ui d = c * 0x772;
	ui e = d * d;
	ui f = d + e;
	ui g = f * 0x474;
	ui h = g * 2;
	return h;
}

int main(){
	printf("I want to find the first token with 0xBEDA as first half.\n");
	for (char c='0'; c<='z'; c++){
		ui first_token = generate_first_token((ui)c);
		printf("%c : 0x%08X\n", c, first_token);
		ui first_half_of_first_token = first_token >> 4 * 4;
		if(first_half_of_first_token == 0xBEDA){
			printf("I FOUND IT!!! -> %c\n", c);
			break;
		}
	}
	return 0;
}