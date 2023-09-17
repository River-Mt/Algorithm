#include <bits/stdc++.h>

using namespace std;

vector<int> solution(vector<int> numbers) {
    vector<int> answer;
    stack<int> st;
    int n = numbers.size() - 1;
    answer.resize(n+1);
    for(int i=n;i>=0;--i) {
        while(1) {
            if(st.empty()) {
                answer[i] = -1;
                break;
            }
            if(st.top() > numbers[i]) {
                answer[i] = st.top();
                break;
            }
            st.pop();
        }
        st.push(numbers[i]);
    }
        
    return answer;
}