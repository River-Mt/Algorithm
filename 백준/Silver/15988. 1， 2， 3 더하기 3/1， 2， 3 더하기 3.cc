#include <iostream>
#include <cstdio>
#include <algorithm>
#include <vector>
#include <cstring>
using namespace std;
#define MOD 1000000009
int tc;
long long dp[1000005];
void getDP() {
    dp[1] = 1;
    dp[2] = 2;
    dp[3] = 4;
    for(int i = 4;i <= 1000001;++i) {
        dp[i] = (dp[i - 1] + dp[i - 2] + dp[i - 3]) % MOD;
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
        cout << dp[n] % MOD << '\n';
    }
 
    return 0;
}
