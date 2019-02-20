#include <iostream>
#include <string>
#include <cmath>

using namespace std;

string code = "AJXGRFV6BKOW3Y9TM4S2ZU I70H5Q81PDECLNAJXGRFV6BKOW3Y9TM4S2ZU I70H5Q81PDECLNAJXGRFV6BKOW3Y9TM4S2ZU I70H5Q81PDECLN";

int string_second_find(string src, char target)
{
	int first_occurrence = src.find(target);
	if(first_occurrence == string::npos) return -1;
	return src.find(target, first_occurrence+1);
}

bool check_serial(string name, string serial)
{
	bool ret = true;
	for(int i=0; i<4; i++){
		long double quater_of_len_of_name = name.length() / 4.0;
		long long quater_index_of_name = (long long)(floor((long double)(quater_of_len_of_name * (i + 1))) - 1.0);
		char quater_char_of_name = name.at((unsigned long long)quater_index_of_name);
		for(int j=3*i; j<3*i+3; j++){
			char quater_char_of_serial = serial.at(j);
			int diff = string_second_find(code, quater_char_of_name) - string_second_find(code, quater_char_of_serial); // WATCH IT!!!!!!! type confusion...
			diff = (diff < 0) ? -diff : diff;
			if(diff > 5){
				return false;
			}
		}
	}
	return ret;
}

// recursive function that find all possibilities.
// 0-9, A-Z, a-z
void recursive_brute_force(string target, string serial)
{
	if(target.length() == 4){
		if(check_serial(target, serial)){
			cout << target << "\n";
		}
		return;
	}
	
	for(char c = '0'; c <= 'Z'; c++){
		if(!(('0'<=c && c<='9') || ('A'<=c && c<='Z'))) continue;
		target += c;
		recursive_brute_force(target, serial);
		target = target.substr(0, target.length() - 1);
	}
}

int main()
{
	string serial = "";
	cout << "Namegen by r4k4" << "\n" << "Enter your Key and I will generate proper names... >> ";
    cin >> serial;
	recursive_brute_force("", serial);
	cout << "\n";
	return 0;
}