#include <iostream>
#include <algorithm>
#include <vector>
#include <queue>
using namespace std;

int n, k, m;
#define TUBE 1005
#define MAX 100005
vector<vector<int>>adj;

int bfs() {
    queue<int>q;
    vector<int>dist(MAX + TUBE, 0);
    q.push(1);
    dist[1] = 1;
    
    while(!q.empty()) {
        int now = q.front();
        q.pop();
        if (now == n) return dist[now];
        for (auto&nx : adj[now]) {
            if (!dist[nx]) {
                dist[nx] = nx > n
                ? dist[now]
                : dist[now] + 1;
                q.push(nx);
            }
        }
    }
    
    return -1;
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    cin >> n >> k >> m;
    adj.resize(MAX + TUBE);
    
    for (int i=1;i<=m;++i) {
        for (int j=0;j<k;++j) {
            int st;
            cin >> st;
            adj[i + n].push_back(st);
            adj[st].push_back(i + n);
        }
    }
    
    cout << bfs() << '\n';
    
    return 0;
}
