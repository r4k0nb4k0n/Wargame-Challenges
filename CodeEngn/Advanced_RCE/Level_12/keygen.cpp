#include <iostream>
#include <sstream>
#include <string>
#include <cstring>
#include <cctype>
#include <iomanip>
#include <algorithm>

using namespace std;

/**
 * 정수값을 16진수 형태의 문자열로 표현.
 * FIX 옵션이 주어질 경우 8개의 16진수로 표현되며 빈 자리는 0을 채운다.
 */
string int_to_hex(int i, string is_fixed)
{
	std::stringstream stream;
	if(!is_fixed.compare("FIX")) stream << setfill('0') << setw(sizeof(int)*2);
	stream << hex << i;
	return stream.str();
}

/*
 * 주어진 Name을 이용하여 Key를 생성.
 */
string generate_key(string name)
{
	string key = "";
	// Generate the first token.
	string ascii_concat = "";
    // Name 한 글자씩 Ascii code 값을 알아내고 이를 하나의 문자열로 이어붙인다.
	for(int i=0; i<name.length(); i++){
		ascii_concat += to_string((int)name[i]);
	}
    // 첫 번째 토큰은 해당 문자열의 5번째 ~ 8번째 글자들이다.
	key += ascii_concat.substr(4, 4);
	key += "-";
	// Generate the second token.
    // 두 번째 토큰은 첫번째 토큰을 음수인 10진수로 읽었을 때,
    // 이를 16진수로 표현하고 마지막 4글자를 사용한다.
	key += int_to_hex(stoi("-" + key.substr(0, 4)), "FIX").substr(4, 4);
	key += "-";
	// Modify the first token.
    // 첫번째 토큰의 3번째 숫자에 14를 더한 값을 16진수로 나타내고 해당 숫자를 대체한다.
	key = key.substr(0, 2) + int_to_hex(stoi(key.substr(2, 1)) + 14, "NOT_FIX") + key.substr(3);
	
	// Generate the third token.
    // 세 번째 토큰의 첫 두 글자는 첫번째 토큰의 첫 숫자에 48을 더한 값이다.
    // 세 번째 토큰의 마지막 두 글자는 Name의 길이에 5를 더한 값을 16진수로 나타낸 것이다.
	key += to_string(stoi(key.substr(0, 1)) + 48);
	key += int_to_hex(name.length() + 5, "FIX").substr(6, 2);
    
	// Make it all upper character.
    // Key에 들어간 알파벳은 모두 대문자로 바꾼다.
    transform(key.begin(), key.end(), key.begin(), ::toupper);
	return key;
}

int main()
{
	string name;
	cin >> name;
	cout << generate_key(name) << "\n";
	return 0;
}