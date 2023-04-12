#include <string>
#include <vector>
#include <algorithm>
#include <iostream>
#include <map>
using namespace std;

vector<int> solution(vector<int> lottos, vector<int> win_nums) {
    vector<int> answer;
    map<int,int>mp;
    mp.insert({6,1});
    mp.insert({5,2});
    mp.insert({4,3});
    mp.insert({3,4});
    mp.insert({2,5});
    mp.insert({1,6});
    mp.insert({0,6});


    int len = 6;
    int erase = 0;
    int wins = 0;
    for(auto& num : lottos) {
        if(!num)erase++;
        else {
            for(auto& win_num : win_nums) {
                if(num == win_num)wins++;
            }
        }
    
    }
    
    answer.push_back(mp[(wins + erase)]);
    answer.push_back(mp[wins]);
    
    return answer;
}
