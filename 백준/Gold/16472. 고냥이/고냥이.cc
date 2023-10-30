#include <cstdio>
#include <iostream>
#include <algorithm>
#include <vector>
#include <queue>
#include <stack>
#include <map>
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
#define MAX 1000005
string s;
int chk[30],n,tmp,ans;
int main(){
    FastIO
    cin>>n>>s;
    int len = (int)s.length();
    int l=0;
    int r=1;
    int cnt=1;
    chk[s[l]-'a']++;
    while(r<len){
        chk[s[r]-'a']++;
        if(chk[s[r]-'a']==1)cnt++;
        while(cnt>n){
            chk[s[l]-'a']--;
            if(chk[s[l]-'a']==0)cnt--;
            l++;
        }
        ans=max(ans,r-l+1);
        r++;
    }
    cout<<ans;
    return 0;
}
