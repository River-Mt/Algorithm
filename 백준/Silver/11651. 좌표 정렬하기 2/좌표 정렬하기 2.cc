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
#include <sstream>
#include <deque>
#include <regex>
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
#define MAX 55
#define all(v) v.begin(), v.end()
#define compress(v) v.erase(unique(all(v)),v.end());

bool cmp(pi& A, pi& B) {
    if(A.second != B.second)return A.second < B.second;
    else return A.first < B.first;
}

int main(){
    FastIO
    int n;
    cin >> n;
    vector<pi> v(n);
    for(int i = 0; i < n; i++)cin >> v[i].first >> v[i].second;
    sort(v.begin(), v.end(), cmp);
    for(auto& x : v) cout << x.first << ' ' << x.second << endl;
    return 0;
}
