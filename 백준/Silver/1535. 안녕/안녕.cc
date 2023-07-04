#include <iostream>
#include <cstdio>
#include <algorithm>
#include <vector>
#include <cstring>
using namespace std;
#define MOD 100999
#define MAX 100005
int n, ans;
int dp[25][105];
int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);
    cin >> n;
    
    vector<int> losts(n + 1);
    vector<int> gets(n + 1);
    
    for(int i=1;i<=n;++i) cin >> losts[i];
    for(int i=1;i<=n;++i) cin >> gets[i];
    
    for(int i=1;i<=n;++i) {
        for(int j=100;j>=0;--j) {
            if(j - losts[i] >= 1)
                dp[i][j] = max(dp[i-1][j],
                               dp[i-1][j-losts[i]] + gets[i]);
            
            else dp[i][j] = dp[i-1][j];

            ans = max(ans, dp[i][j]);
        }
    }
        
    cout << ans << '\n';
    
    return 0;
}
