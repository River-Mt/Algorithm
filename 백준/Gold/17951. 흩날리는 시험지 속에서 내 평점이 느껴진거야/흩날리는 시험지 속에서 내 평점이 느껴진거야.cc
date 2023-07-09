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
#define MAX 10005
#define x first
#define y second
#define all(v) v.begin(), v.end()
#define compress(v) v.erase(unique(all(v)),v.end())
int n,g,l,r,ans;
vector<int>v;
int main(){
    FastIO
    cin>>n>>g;
    v.resize(n+1);
    v[0]=0;
    for(int i=1;i<=n;++i)cin>>v[i],r+=v[i],v[i]=r;
    while(l<=r){
        int mid = (l+r)/2, cnt = 0, sum = 0,st = 0;
        for(int i=1;i<=n;++i){
            if(v[i]-v[st] >= mid){
                st = i;
                cnt++;
            }
        }
        if(cnt<g)r=mid-1;
        else{
            l = mid+1;
            ans = max(ans,mid);
        }
    }
    cout<<ans<<endl;
    return 0;
}
