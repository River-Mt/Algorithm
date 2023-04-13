#include <string>
#include <vector>
#include <map>
#include <set>
#include <iostream>
using namespace std;

bool solution(vector<string> phone_book) {
    bool answer = true;
    int cnt = 0;
    set<string> st;
    
    for(auto s : phone_book)st.insert(s);
    
    for(auto s : phone_book) {
        for(int i=0;i<s.size();++i) {
            if(st.find(s.substr(0,i+1)) != st.end()) cnt++;
        }
    }
        
    return (cnt == phone_book.size()) ? true : false;
}