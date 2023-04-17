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

int n, m, ans;
char arr[MAX][MAX];

int main(){
    FastIO
    cin >> n >> m;
    for(int i = 1; i <= n; i++)
        for(int j = 1; j <= m; j++)
            cin >> arr[i][j];
    
    ans = 1;
    
    for (int k = 1; k <= max(n, m); k++) {
        for(int i = 1; i <= n; i++) {
            for(int j = 1; j <= m; j++) {
                if(i + k > n || j + k > m) continue;
                char lu = arr[i][j];
                char ru = arr[i][j + k];
                if(lu != ru) continue;
                char ld = arr[i + k][j];
                if(lu != ld) continue;
                char rd = arr[i + k][j + k];
                if(lu != rd) continue;
                ans = max(ans, (k+1)*(k+1));
            }
        }
    }
    
    cout << ans << endl;
    
    return 0;
}
