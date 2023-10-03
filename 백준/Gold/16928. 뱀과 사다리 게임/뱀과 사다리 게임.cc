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
#define MAX 101
#define x first
#define y second
#define all(v) v.begin(), v.end()
/*
 BOJ 16928 뱀과 사다리 게임
 주사위를 굴려 한 행에서 주사위 수 만큼 이동
 사다리 또는 뱀이 있는 곳으로 이동한다면 연결된 곳으로 이동
 */
int n,m;
int board[MAX],chk[MAX],jump[MAX];
int ans;
void bfs(){
    queue<pi>q;
    q.push({1,0});
    ans = INF;
    while(!q.empty()){
        int now = q.front().first;
        int cnt = q.front().second;
        q.pop();
        chk[now]=1;
        if(now==100){
            ans = cnt;
            return;
        }
        for(int i=1;i<=6;++i){
            int nx = (!jump[now+i])?now+i:jump[now+i];
            if(nx>100)continue;
            if(chk[nx])continue;
            q.push({nx,cnt+1});
        }
    }
}
int main(){
    FastIO
    cin>>n>>m;
    for(int i=0,a,b;i<n+m;++i){
        cin>>a>>b;
        jump[a]=b;
    }
    bfs();
    cout<<ans;
    return 0;
}

