#include <cstdio>
#include <iostream>
#include <algorithm>
#include <vector>
#include <queue>
#include <stack>
#include <map>
#include <set>
#include <string>
#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <deque>
using namespace std;
#define ll long long
#define pi pair<int,int>
#define ppi pair<int,pair<int,int>>
#define pll pair<ll,ll>
#define FOR(a,n) for(int i=a;i<n;++i)
#define FastIO ios_base::sync_with_stdio(false);cin.tie(NULL);cout.tie(NULL);
#define vvi vector<vector<int>>
#define vi vector<int>
#define vpi vector<pair<int,int>>
#define endl '\n'
#define INF 987654321
#define MOD 1000000000
#define MAX 1000005
#define all(v) v.begin(), v.end()
/*
 boj 9370 미확인 도착지
 
 algorithm : 다익스트라
 
 출발점은 하나, 목적지는 후보들 중 하나
 목적지까지 최단거리로 이동
 이때, g, h 사이를 들려서 이동함 (g != h)
 
 todo : 가능한 목적지들을 오름차순으로 출력

 */
int n, m, t, s, g, h;
void dijk(vector<int>&dist, vector<vector<pi>>&adj, int source){
    priority_queue<pi>pq;
    pq.push({0, source});
    dist[source] = 0;
    
    while(!pq.empty()){
        int now = pq.top().second;
        int cost = -pq.top().first;
        pq.pop();
        if(dist[now] < cost)continue;
        for(auto& nx : adj[now]){
            int nx_node = nx.second;
            int nx_cost = cost + nx.first;
            if(dist[nx_node] > nx_cost){
                dist[nx_node] = nx_cost;
                pq.push({-nx_cost, nx_node});
            }
        }
    }
}

void solve(){
    cin >> n >> m >> t; // 교차로(노드), 도로(간선), 목적지 후보 개수
    cin >> s >> g >> h; // source, 경유지
    
    vector<int>s_dist(n + 1, INF);
    vector<int>g_dist(n + 1, INF);
    vector<int>h_dist(n + 1, INF);
    vector<int>sinks;
    vector<vector<pi>>adj;
    adj.resize(n + 1);
    
    for(int i=0;i<m;++i){
        int u, v, d;
        cin >> u >> v >> d;
        adj[u].push_back({d,v});
        adj[v].push_back({d,u});
    }
    
    for(int i=0;i<t;++i){
        int sink;
        cin >> sink;
        sinks.push_back(sink);
    }
    
    sort(all(sinks));
    
    dijk(s_dist, adj, s);
    dijk(g_dist, adj, g);
    dijk(h_dist, adj, h);
    
    for(auto& sink : sinks){
        int path1 = s_dist[g] + g_dist[h] + h_dist[sink];
        int path2 = s_dist[h] + h_dist[g] + g_dist[sink];
        
        if(s_dist[sink] == min(path1, path2))cout << sink  << ' ';
    }
    cout << endl;
    
}

int main() {
    FastIO
    int tc;
    cin >> tc;
    while(tc--)solve();
    return 0;
}
