#include <string>
#include <vector>
#include <algorithm>
#include <iostream>
using namespace std;

vector<int> solution(vector<int> array, vector<vector<int>> commands) {
    vector<int> answer;
    for(auto& com : commands) {
        vector<int> tmp = array;
        int i = com[0];
        int j = com[1];
        int k = com[2];
        
        sort(tmp.begin() + i - 1, tmp.begin() + j);
        answer.push_back(tmp[i + k - 2]);
    }
    return answer;
}