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
#define INF 1000000
#define MOD 1000000000
#define MAX 100005
#define x first
#define y second
#define all(v) v.begin(), v.end()
int n,k,m;
vector<int>adj[MAX+1000];
int dist[MAX+1000];

int bfs(){
    queue<int>q;
    dist[1]=1;
    q.push(1);
    while(!q.empty()){
        int now = q.front();
        q.pop();
        if(now == n)return dist[now];
        for(auto& nx : adj[now]){
            if(dist[nx])continue;
            dist[nx] = (nx>n) ? dist[now] : dist[now]+1;
            q.push(nx);
        }
    }
    return -1;
}

int main(){
    FastIO
    cin>>n>>k>>m;
    for(int i=1;i<=m;++i){
        for(int j=1,h;j<=k;++j){
            cin>>h;
            adj[h].push_back(i+n);
            adj[i+n].push_back(h);
        }
    }
    cout<<bfs()<<endl;
    
    return 0;
}
