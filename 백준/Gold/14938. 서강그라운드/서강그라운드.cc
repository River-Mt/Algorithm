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
#define INF 1e9
#define MOD 1000000000
#define MAX 105
#define all(v) v.begin(), v.end()
int dist[MAX][MAX],item[MAX],n,m,r,ans;
int main(){
    FastIO
    cin>>n>>m>>r;
    for(int i=0;i<n;++i)cin>>item[i];
    for(int i=0;i<n;++i)for(int j=0;j<n;++j)dist[i][j]=(i==j)?0:INF;
    for(int i=0;i<r;++i){
        int u,v,c;
        cin>>u>>v>>c;
        dist[u-1][v-1]=dist[v-1][u-1]=c;
    }
    for(int k=0;k<n;++k)
        for(int i=0;i<n;++i)
            for(int j=0;j<n;++j)
                dist[i][j] = min(dist[i][j],dist[i][k]+dist[k][j]);
    for(int i=0;i<n;++i){
        int sum = 0;
        for(int j=0;j<n;++j){
            if(dist[i][j]<=m)sum+=item[j];
        }
        ans = max(ans,sum);
    }
    cout<<ans;
    return 0;
}
