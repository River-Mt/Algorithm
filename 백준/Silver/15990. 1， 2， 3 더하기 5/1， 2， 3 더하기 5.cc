#include <iostream>
#include <cstdio>
#include <algorithm>
#include <vector>
#include <cstring>
using namespace std;
#define MOD 1000000009
#define MAX 100005
int tc;
long long dp[MAX][4];
void getDP() {
    dp[1][1] = dp[2][2] = 1;
    dp[3][1] = dp[3][2] = dp[3][3] = 1;
    for(int i=4;i<=MAX;++i) {
        dp[i][1] = (dp[i-1][2] + dp[i-1][3]) % MOD;
        dp[i][2] = (dp[i-2][1] + dp[i-2][3]) % MOD;
        dp[i][3] = (dp[i-3][1] + dp[i-3][2]) % MOD;
    }
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);
    cin >> tc;
    getDP();
    while(tc--) {
        int n;
        cin >> n;
        cout << (dp[n][1] + dp[n][2] + dp[n][3]) % MOD << '\n';
    }
 
    return 0;
}
