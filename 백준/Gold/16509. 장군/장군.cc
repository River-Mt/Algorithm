#include <cstdio>
#include <iostream>
#include <algorithm>
#include <vector>
#include <queue>
#include <stack>
#include <map>
#include <string>
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
int dr[]={-2,-3,-3,-2,2,3,3,2};
int dc[]={-3,-2,2,3,3,2,-2,-3};
int ddr[]={0,-1,-1,0,0,1,1,0};
int ddc[]={-1,0,0,1,1,0,0,-1};
int dddr[]={-1,-2,-2,-1,1,2,2,-1};
int dddc[]={-2,-1,1,2,2,1,-1,-2};
int v[11][11];
int sR,sC;
int kR,kC;

int bfs(){
    queue<ppi>q;
    q.push({1,{sR,sC}});
    v[sR][sC]=1;
    
    while(!q.empty()){
        int r = q.front().second.first, c = q.front().second.second, cnt = q.front().first;
        q.pop();
        for(int i=0;i<8;++i){
            int nr = r + dr[i], nc = c + dc[i];
            int nnr = r + ddr[i], nnc = c + ddc[i];
            int nnnr = r + dddr[i], nnnc = c + dddc[i];
            if(nr<0||nc<0||nr>=10||nc>=9)continue;
            if(nnr<0||nnc<0||nnr>=10||nnc>=9)continue;
            if(nnnr<0||nnnc<0||nnr>=10||nnnc>=9)continue;
            if(nnr==kR&&nnc==kC)continue;
            if(nnnr==kR&nnnc==kC)continue;
            if(v[nr][nc])continue;
            if(nr==kR&&nc==kC)return cnt;
            q.push({cnt+1,{nr,nc}});
            v[nr][nc]=1;
        }
    }
    return -1;
}

int main(){
    cin>>sR>>sC>>kR>>kC;
    cout<<bfs();
    
    return 0;
}
