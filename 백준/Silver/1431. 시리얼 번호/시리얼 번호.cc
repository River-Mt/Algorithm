#include <iostream>
#include <algorithm>
#include <vector>
#include <string>
#include <cctype>
using namespace std;
typedef pair<int, int> pi;
#define endl '\n'
#define MAX 10005
#define FIO ios_base::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);

int n;
vector<string> v;

int getSum(string s) {
    int sum = 0;
    
    for(auto&ch : s)
        if(isdigit(ch))sum += ch - '0';
    
    return sum;
}

bool cmp(string&A, string &B) {
    if(A.length() != B.length())return A.length() < B.length();
    else if(getSum(A) != getSum(B)) return getSum(A) < getSum(B);
    else return A < B;
}

int main() {
    FIO
    cin >> n;
    v.resize(n);
    
    for(int i = 0; i < n; i++)cin >> v[i];
    sort(v.begin(), v.end(), cmp);
    
    for(auto&s : v)cout << s << endl;
    
    return 0;
}
