#include <iostream>
#include <queue>
#include <algorithm>
#include <vector>
#include <string>
#include <map>
#include <set>
using namespace std;
#define ll long long
typedef pair<int, int> pi;
int n, q;
vector<vector<pi>> adj;

int bfs(int s, int k) {
    queue<int> q;
    vector<int> chk(n + 1, 0);
    int cnt = 0;
    q.push(s);
    chk[s] = 1;
    while(!q.empty()) {
        int cur = q.front();
        q.pop();
        for(auto&node : adj[cur]) {
            int nx = node.first;
            int usado = node.second;
            if(chk[nx] || usado < k) continue;
            chk[nx] = 1;
            cnt++;
            q.push(nx);
        }
    }
    return cnt;
}
int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);
    cin >> n >> q;
    adj.resize(n + 1);
    for(int i=0;i<n-1;++i) {
        int u, v, c;
        cin >> u >> v >> c;
        adj[u].push_back({v, c});
        adj[v].push_back({u, c});
    }
    for(int i=0;i<q;++i) {
        int s, k;
        cin >> k >> s;
        cout << bfs(s, k) << '\n';
    }
    return 0;
}
         
