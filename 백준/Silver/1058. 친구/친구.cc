#include <iostream>
#include <cstdio>
#include <algorithm>
#include <queue>
#include <vector>
#include <cstring>
using namespace std;

int n;
vector<string>f;
vector<vector<int>> adj;
int chk[55];

void init_Graph() {
    for(int i=0;i<n;++i) {
        for (int j=0;j<n;++j) {
            if(f[i][j] == 'N') continue;
            else adj[i].push_back(j);
        }
    }
}

int bfs(int cur) {
    queue<int> q;
    vector<int> dist(n, 0);
    q.push(cur);
    dist[cur] = 1;
    int ret = 0;
    while(!q.empty()) {
        int now = q.front();
        q.pop();
        if(dist[now] > 2) continue;
        for(auto&nx : adj[now]) {
            if(dist[nx]) continue;
            ret += 1;
            dist[nx] = dist[now] + 1;
            q.push(nx);
        }
    }
    return ret;
}

void solve() {
    int ans = 0;
    init_Graph();
    for(int i=0;i<n;++i) {
        memset(chk, 0, sizeof(chk));
        ans = max(ans, bfs(i));
    }
    cout << ans << endl;
    
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    cin >> n;
    f.resize(n);
    adj.resize(n);
    for(int i=0;i<n;++i) cin >> f[i];
    solve();
    
    return 0;
}
