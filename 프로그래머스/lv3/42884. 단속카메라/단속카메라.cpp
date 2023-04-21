#include <string>
#include <vector>
#include <algorithm>
#include <queue>
using namespace std;

int solution(vector<vector<int>> routes) {
    int answer = 0;
    vector<pair<int, int>>v;
    for(auto& route : routes) {
        v.push_back({route[1], route[0]});
    }
    
    sort(v.begin(), v.end());
    
    int camLoc = -30001;
    
    for(auto&x : v) {
        int ed = x.first;
        int st = x.second;
        if(st > camLoc) {
            answer++;
            camLoc = ed;
        }
    }
    
    return answer;
}