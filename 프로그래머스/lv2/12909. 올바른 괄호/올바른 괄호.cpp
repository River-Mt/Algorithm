#include <string>
#include <iostream>
#include <stack>
#include <vector>
using namespace std;

bool solve(string s) {
    stack<char> st;
    for(auto&ch : s) {
        if(ch == '(') st.push(ch);
        else {
            if(st.empty()) return false;
            else st.pop();
        } 
    }
    return st.empty() ? true : false;
}

bool solution(string s)
{
    bool answer = true;
    return answer = solve(s);
}