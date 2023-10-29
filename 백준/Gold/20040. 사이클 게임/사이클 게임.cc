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
#define MAX 5e5+1
vector<int>cost;
int n,m,cnt;
struct UF{
    vector<int>par;
    UF(int n) : par(n){
        for(int i=0;i<n;++i)par[i]=-1;
    }
    int find(int u){
        return par[u]<0 ? u : par[u] = find(par[u]);
    }
    int merge(int u,int v){
        u = find(u);
        v = find(v);
        if(u==v)return 0;
        if(par[u]<par[v])swap(u,v);
        par[v]+=par[u];
        par[u]=v;
        return 1;
    }
   
};

int main(){
    FastIO
    cin>>n>>m;
    UF uf(n);
    for(int i=1;i<=m;++i){
        int v,w;
        cin>>v>>w;
        if(!uf.merge(v, w)){
            cout<<i;
            return 0;
        }
    }
    cout<<0;
    return 0;
}
