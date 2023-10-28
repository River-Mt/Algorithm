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
#define FOR(I,S,N) for(int I=S;I<=N;++I)
#define FastIO ios_base::sync_with_stdio(false);cin.tie(NULL);cout.tie(NULL);
#define vvi vector<vector<int>>
#define vi vector<int>
#define vpi vector<pair<int,int>>
#define INF 1e9
#define MOD 1000000000
#define MAX 1e6+5
vector<int>cost;
int n,m,k;
struct UF{
    vector<int>par,minCost;
    UF(int n) : par(n+1),minCost(n+1){
        for(int i=1;i<=n;++i)par[i]=-1;
        for(int i=1;i<=n;++i)minCost[i]=cost[i];
    }
    int find(int u){
        return par[u]<0 ? u : par[u] = find(par[u]);
    }
    void merge(int u,int v){
        u = find(u);
        v = find(v);
        if(u==v)return;
        if(par[u]<par[v])swap(u,v);
        par[v]+=par[u];
        par[u]=v;
        minCost[v] = min(minCost[u],minCost[v]);
    }
    void make_friend(){
        int sum=0;
        for(int i=1;i<=n;++i){
            if(par[i]<0)sum+=minCost[i];
            if(sum>k){
                cout<<"Oh no";
                return;
            }
        }
        cout<<sum;
    }
};

int main(){
    FastIO
    cin>>n>>m>>k;
    cost.resize(n+1);
    for(int i=1;i<=n;++i)cin>>cost[i];
    UF uf(n);
    for(int i=1;i<=m;++i){
        int v,w;
        cin>>v>>w;
        uf.merge(v, w);
    }
    uf.make_friend();
    return 0;
}
