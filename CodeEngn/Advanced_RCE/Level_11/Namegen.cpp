#include <iostream>
#include <string>
#include <cstdlib>
#define MAX_LENGTH 10

typedef unsigned int ui;

using namespace std;

ui rol(ui target, int num)
{
	return (target << num) | (target >> (sizeof(target) * 8 - num));
}

string generate_serial(string name)
{
	string serial = "";
	ui sum = 0x78 * 0x7E;
	ui md8 = (ui)('m' * ('d' + '8'));
	for(int i=0; i<name.length(); i++){
		char ch = name[i];
		sum += (ui)ch * md8;
	}
	ui dividend = sum;
	ui divisor = 0x0F;
	while(dividend > 0){
		ui quotient = dividend / divisor;
		ui remainder = dividend % divisor;
		dividend = quotient;
		ui candidate = remainder + 0x30;
		if(0x39 < candidate) serial += (char)(candidate + 0x08); 
		else serial += (char)candidate;
		dividend = rol(dividend, 1);
	}
	return serial;
}

string generate_random_alnum()
{
	static const char alphanum[] = 
		"0123456789"
		"ABCDEFGHIJKLMNOPQRSTUVWXYZ"
		"abcdefghijklmnopqrstuvwxyz";
	string ret = "";
	int len = rand() % MAX_LENGTH;
	for(int i=0; i<len; ++i){
		ret += alphanum[rand() % (sizeof(alphanum) - 1)];
	}

	return ret;
}

int main()
{
	string target = "94E7DB1B";
	while(1){
		string name = generate_random_alnum();
		string serial = generate_serial(name);
		if(serial.compare(target)==0){
			cout << "Gotcha!!! " << name << " -> " << serial << "\n";
			cin.get();
		}
		if(serial[0] == '9'){
			cout << "Sniff Sniff... " << name << " -> " << serial << "\n";
		}
	}
	return 0;
}