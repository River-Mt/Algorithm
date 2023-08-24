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
#define MAX 70
#define x first
#define y second
int n,arr[MAX][MAX];
string s[MAX];

void quad(int len,int r,int c){
    if(!len)return;
    int sum = 0;
    for(int i=r;i<r+len;++i)for(int j=c;j<c+len;++j)sum += arr[i][j];
    if(sum==0){
        cout<<0;
        return;
    }
    else if(sum==len*len){
        cout<<1;
        return;
    }
    pi lu = {r,c}, ru = {r,c+len/2}, ld = {r+len/2,c}, rd = {r+len/2,c+len/2};
    cout<<'(';
    quad(len/2,lu.x,lu.y);
    quad(len/2,ru.x,ru.y);
    quad(len/2,ld.x,ld.y);
    quad(len/2,rd.x,rd.y);
    cout<<')';
    return;
}

int main(){
    FastIO
    cin>>n;
    for(int i=0;i<n;++i)cin>>s[i];
    for(int i=0;i<n;i++)for(int j=0;j<n;++j)arr[i][j] = s[i][j] - '0';
    quad(n,0,0);
    return 0;
}
