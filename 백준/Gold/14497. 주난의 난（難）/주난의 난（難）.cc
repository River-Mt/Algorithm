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
#define MAX 305
#define all(v) v.begin(), v.end()
int n,m,sr,sc,tr,tc,ans;
string arr[MAX];
int chk[MAX][MAX];
int dr[]={0,0,-1,1},dc[]={-1,1,0,0};
struct node{
    int x,y,c;
};
bool bfs(){
    queue<node>q;
    memset(chk,0,sizeof(chk));
    q.push({sr,sc,1});
    chk[sr][sc]=1;
    while(!q.empty()){
        int r = q.front().x, c = q.front().y, cnt = q.front().c;
        q.pop();
        if(r==tr&&c==tc){
            return true;
        }
        for(int i=0;i<4;++i){
            int nr = r+dr[i], nc = c+dc[i];
            if(nr<0||nc<0||nr>=n||nc>=m||chk[nr][nc])continue;
            chk[nr][nc]=1;
            if(arr[nr][nc]=='1'){
                arr[nr][nc]='0';
            }
            else q.push({nr,nc,cnt});
        }
    }
    return false;
}

int main(){
    FastIO
    cin>>n>>m;
    cin>>sr>>sc>>tr>>tc;
    for(int i=0;i<n;++i)cin>>arr[i];
    sr-=1;
    sc-=1;
    tr-=1;
    tc-=1;
    ans = 1;
    while(!bfs())ans++;
    cout<<ans;
    return 0;
}
