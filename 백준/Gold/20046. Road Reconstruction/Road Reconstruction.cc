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
#define MAX 1005
#define x first
#define y second
#define all(v) v.begin(), v.end()
#define compress(v) v.erase(unique(all(v)),v.end())
int m,n,city[MAX][MAX],d[MAX][MAX];
priority_queue<pair<int,pi>>pq;
int dr[]={-1,1,0,0},dc[]={0,0,-1,1};
void dijk(){
    if(city[0][0]==-1)return;
    pq.push({-city[0][0],{0,0}});
    d[0][0]=city[0][0];
    while(!pq.empty()){
        int r = pq.top().second.first;
        int c = pq.top().second.second;
        int val = -pq.top().first;
        pq.pop();
        if(d[r][c]<val)continue;
        for(int i=0;i<4;++i){
            int nr = r+dr[i], nc = c+dc[i];
            if(nr<0||nc<0||nr>=m||nc>=n||city[nr][nc]==-1)continue;
            int cost = val+city[nr][nc];
            if(d[nr][nc]>cost){
                d[nr][nc] = cost;
                pq.push({-cost,{nr,nc}});
            }
        }
    }
}

int main(){
    FastIO
    cin>>m>>n;
    for(int i=0;i<m;++i)for(int j=0;j<n;++j)cin>>city[i][j],d[i][j]=INF;
    dijk();
    cout<<(d[m-1][n-1]==INF?-1:d[m-1][n-1])<<endl;
    return 0;
}
