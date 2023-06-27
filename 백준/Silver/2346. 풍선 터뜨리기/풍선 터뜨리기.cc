#include <cstdio>
#include <algorithm>
#include <deque>
#include <vector>
#include <iostream>
using namespace std;
typedef pair<int, int> pi;
int n;
deque<pi> dq;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    cin >> n;
    
    for(int i=1, move;i<=n;++i) {
        cin >> move;
        dq.push_back({i, move});
    }
    
    while(!dq.empty()) {
        int move = dq.front().second;
        cout << dq.front().first << ' ';
        dq.pop_front();
        
        if(move < 0) {
            move *= -1;
            while(move--) {
                dq.push_front(dq.back());
                dq.pop_back();
            }
        }
        
        else {
            move -= 1;
            while(move--) {
                dq.push_back(dq.front());
                dq.pop_front();
            }
        }
    }
    return 0;
}
