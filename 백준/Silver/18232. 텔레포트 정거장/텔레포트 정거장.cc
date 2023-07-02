#include <iostream>
#include <queue>
#include <algorithm>
#include <vector>
#include <string>
#include <map>
using namespace std;
#define ll long long
int n, m, s, e;
vector<vector<int>> adj;
void bfs() {
    vector<int>dist(n + 1, 0);
    queue<int> q;
    q.push(s);
    dist[s] = 1;
    
    while(!q.empty()) {
        int now = q.front();
        q.pop();
        if(now == e) {
            cout << dist[now] - 1;
            return;
        }
        for(auto&nx : adj[now]) {
            if(dist[nx])continue;
            dist[nx] = dist[now] + 1;
            q.push(nx);
        }
        if(now + 1 <= n && !dist[now + 1]) {
            dist[now + 1] = dist[now] + 1;
            q.push(now + 1);
        }
        
        if(now - 1 >= 1 && !dist[now - 1]) {
            dist[now - 1] = dist[now] + 1;
            q.push(now - 1);
        }
    }
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);
    cin >> n >> m;
    cin >> s >> e;
    adj.resize(n + 1);
    for(int i=0;i<m;++i) {
        int x, y;
        cin >> x >> y;
        adj[x].push_back(y);
        adj[y].push_back(x);
    }
    
    bfs();
    
    return 0;
}
         
