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

int n;
vector<string> files;
map<string, int> mp;

int main(){
    FastIO
    cin >> n;
    files.resize(n);
    for(int i = 0; i < n; i++) cin >> files[i];
    
    for(string file: files) {
        string name;
        string extender;
        stringstream ss(file);
        while(getline(ss, name, '.') && ss >> extender) mp[extender]++;
    }
    
    for(auto&[a,b] : mp) cout << a << ' ' << b << endl;

    return 0;
}
