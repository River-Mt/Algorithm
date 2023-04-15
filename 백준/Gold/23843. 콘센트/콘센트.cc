#include <iostream>
#include <algorithm>
#include <vector>
#include <cmath>
#include <queue>
using namespace std;
#define FIO ios_base::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);
#define endl '\n'
int n, m;
vector<int>v;
priority_queue<int> pq;

int main() {
    FIO
    cin >> n >> m;
    
    for(int i = 0; i < n; ++i) {
        int num;
        cin >> num;
        v.push_back(-num);
    }
    
    sort(v.begin(), v.end());
    
    for(int i = 0; i < m; ++i) pq.push(v[i]);
    
    for(int i = m; i < n; ++i) {
        int minCharge = pq.top();
        pq.pop();
        pq.push(minCharge + v[i]);
    }
    
    int ans = 0;
    
    while(!pq.empty()) ans = max(ans, -pq.top()), pq.pop();
    
    cout << ans << endl;
    
    return 0;
}

