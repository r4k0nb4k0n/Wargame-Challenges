/*
 * Unlock Code must be 7-16 characters.
 * Key generated from Unlock Code must be 37(0x25)
**/

#include <iostream>
#include <string>
#include <cstdlib>
#define MAX_LENGTH 16

typedef unsigned int ui;
typedef unsigned short us;

using namespace std;

ui generate_key(string unlock_code)
{
	int index = -1;
	ui key = 0;
	for (int l=0x10; l>=0; l--){
		int i = 0;
		if(index < unlock_code.length()) i = index;
		ui a = l * l;
		a = ((a >> (2 * 8)) + (a & 0xFF)) & 0xFF;
		ui b = (i != -1) ? (ui)unlock_code[i] : 0x00;
		ui c = (a * b);
		c = ((c >> (2 * 8)) + (c & 0xFF)) & 0xFF;
		key += c;
	}
	key = key & 0xFF;
	return key;
}

string generate_random_alnum()
{
	static const char alphanum[] = 
		"0123456789";
	string ret = "";
	int len = rand() % MAX_LENGTH;
	if (len < 8) len = 8;
	for(int i=0; i<len; ++i){
		ret += alphanum[rand() % (sizeof(alphanum) - 1)];
	}
	return ret;
}

int main()
{
	ui target = 0x25;
	while(1){
		string unlock_code = generate_random_alnum();
		ui key = generate_key(unlock_code);
		if(key == target){
			cout << "Gotcha!!! " << unlock_code << " -> " << key << "\n";
			break;
		}
	}
	return 0;
}