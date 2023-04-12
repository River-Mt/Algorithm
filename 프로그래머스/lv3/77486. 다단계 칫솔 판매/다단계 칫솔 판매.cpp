#include <string>
#include <vector>
#include <map>
#include <iostream>
using namespace std;
map<string, string> par;
map<string, int> earns;

void cacl(string human, int amount) {
    if(human == "-") return;
    int div = amount * 0.1;
    earns[human] += amount - div; 
    if(div < 1)return;
    cacl(par[human], div);
}

vector<int> solution(vector<string> enroll, vector<string> referral, vector<string> seller, vector<int> amount) {
    vector<int> answer;
    int n = (int)enroll.size();
    
    for(int i=0;i<n;++i) par.insert({enroll[i], referral[i]});
    
    for(auto& val : amount) val *= 100;
    
    for(int i=0;i<(int)seller.size();++i) cacl(seller[i], amount[i]);
    
    for(auto& name : enroll) answer.push_back(earns[name]);
    
    return answer;
}