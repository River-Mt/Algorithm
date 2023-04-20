#include <string>
#include <vector>
#include <algorithm>
#include <queue>
#include <stack>
#include <iostream>
#include <cmath>
#include <bitset>

using namespace std;

string getFullBinary(string str) {
    string ret = str;
    int idx = 2;
    int len = str.length();
    while (true) {
        if (len <= idx - 1) break;
        idx *= 2;
    }
    for (int i = 0; i < idx - 1 - len; i++) ret += '0';
    return ret;
}

string toBinary(long long number) {
    string bits;
    
    while(number) {
        bits += (number%2) + '0';
        number /= 2;
    }
    
    int bits_size = bits.size();
    
    string full = getFullBinary(bits);
    
    reverse(full.begin(), full.end());
    

    return full;
}

bool checkAllZero(string state) {
    for(auto&bit : state)
        if(bit == '1')return false;
    
    return true;
}

bool search(string state) {
    if(checkAllZero(state))return true;
    if(state.length() == 1)return true;
    
    int len = state.length();
    int mid = len/2;
    string left = state.substr(0, mid);
    string right = state.substr(mid + 1);
    
    if(state[mid] == '1' && search(left) && search(right)) return true;
    else return false;
    
}

vector<int> solution(vector<long long> numbers) {
    vector<int> answer;
    
    for(auto& number : numbers) {
        string bits = toBinary(number);
        answer.push_back(search(bits));
    }
    
    
    return answer;
}