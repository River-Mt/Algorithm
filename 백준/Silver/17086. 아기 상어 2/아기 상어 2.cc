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
#define FOR(n) for(int i=0;i<n;++i)
#define FFOR(n,m) for(int i=0;i<n;++i)for(int j=0;j<m;++j)
#define FastIO ios_base::sync_with_stdio(false);cin.tie(NULL);cout.tie(NULL);
#define vvi vector<vector<int>>
#define vi vector<int>
#define vpi vector<pair<int,int>>
#define endl '\n'
#define INF 1e10
#define MOD 1000000000
#define MAX 100005
#define all(v) v.begin(), v.end()
#define compress(v) v.erase(unique(all(v)),v.end())
#include <string>
#include <vector>
#include <set>
#include <iostream>
using namespace std;
#include <cstdio>
#include <algorithm>
#include <vector>
#include <queue>
#include <set>
using namespace std;
int n,m,ans;
int arr[55][55], dist[55][55];
int dr[] = {0,0,-1,1,-1,-1,1,1};
int dc[] = {-1,1,0,0,-1,1,1,-1};
queue<pi>q;

void bfs(){
    while(!q.empty()){
        int r = q.front().first;
        int c = q.front().second;
        q.pop();
        ans = max(dist[r][c],ans);
        for(int i=0;i<8;++i){
            int nr = r+dr[i];
            int nc = c+dc[i];
            if(nr<0||nc<0||nr>=n||nc>=m)continue;
            if(dist[nr][nc])continue;
            dist[nr][nc] = dist[r][c]+1;
            q.push({nr,nc});
        }
        
    }
}

int main(){
    FastIO
    cin>>n>>m;
    for(int i=0;i<n;++i){
        for(int j=0;j<m;++j){
            cin>>arr[i][j];
            if(arr[i][j]){
                q.push({i,j});
                dist[i][j]=1;
            }
        }
    }
    bfs();
    cout<<ans-1<<endl;
    
    return 0;
}

