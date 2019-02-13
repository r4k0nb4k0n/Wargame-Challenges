#include <cstdio>
#include <cstring>

typedef unsigned int ui;

ui generate_first_token(char name[])
{
	ui c, d, e, f, g, h=0, seed;
	for (int i=0; i<strlen(name); i++){
		seed = (ui)name[i];
		c = seed + h;
		d = c * 0x772;
		e = d * d;
		f = d + e;
		g = f * 0x474;
		h = g * 2;
	}
	return h;
}

int main(){
	printf("5D88-53B4-52A87D27-1D0D-5B09\n");
	printf("I want to find the first token with 0x5D88 as first half.\n");
	for (char c='0'; c<='z'; c++){
		for(char d='0'; d<='z'; d++){
			char name[3] = {c, d, '\0'};
			ui first_token = generate_first_token(name);
			if(d=='z') printf("%s : 0x%08X\n", name, first_token);
			ui first_half_of_first_token = first_token >> 4 * 4;
			if(first_half_of_first_token == 0x5D88){
				printf("I FOUND IT!!! -> %s : 0x%08X\n", name, first_token);
				return 0;
			}
		}
	}
	return 0;
}