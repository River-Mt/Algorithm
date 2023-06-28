#include <iostream>
#include <queue>
#include <algorithm>
#include <vector>
#include <string>
using namespace std;
int n;
string ans;
bool isExistSubString(string s) {
    for(int i=1;i<=s.length()/2;++i) {
        string back = s.substr(s.length() - i, i);
        string front = s.substr(s.length() - i * 2, i);
                
        if (front == back) return true;
        
    }
    return false;
}

bool btrc(string s) {
    if(isExistSubString(s)) return false;
    
    if(s.length() >= n) {
        ans = s;
        return true;
    }
    
    for(int i=1;i<=3;++i) {
        s.push_back(i + '0');
        if (btrc(s) == true) return true;
        s.pop_back();
    }
    return false;
}

int main() {
    cin >> n;
    btrc("");
    cout << ans;
    return 0;
}
