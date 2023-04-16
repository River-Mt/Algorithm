#include <iostream>
#include <algorithm>
#include <vector>
#include <cmath>
#include <queue>
#include <stack>
using namespace std;
#define FIO ios_base::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);
#define endl '\n'
string org, bomb;

string solve() {
    stack<char> st;
    int bombSize = (int)bomb.size();
    char bombEnd = bomb[bombSize-1];
    
    for(auto& ch : org) {
        st.push(ch);
        if(ch == bombEnd) {
            stack<char> tmp;
            bool flag = false;
            for(int i = bombSize - 1; i >= 0; --i) {
                if(st.empty()) {
                    flag = true;
                    while(!tmp.empty()) {
                        st.push(tmp.top());
                        tmp.pop();
                    }
                    break;
                }
                
                char top = st.top();
                
                if(top == bomb[i]) {
                    st.pop();
                    tmp.push(top);
                }
                
                else {
                    flag = true;
                    while(!tmp.empty()) {
                        st.push(tmp.top());
                        tmp.pop();
                    }
                    break;
                }
            }
            
        }
    }
    if(st.empty()) return "FRULA";
    string ans = "";
    
    while(!st.empty()){
        ans+=st.top();
        st.pop();
    }
    
    reverse(ans.begin(), ans.end());
    return ans;
}

int main() {
    FIO
    cin >> org >> bomb;
    cout << solve() << endl;
    return 0;
}

