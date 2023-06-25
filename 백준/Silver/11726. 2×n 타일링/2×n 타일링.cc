#include <iostream>
#include <algorithm>
#include <vector>
#include <queue>
#include <string>
#include <cstdlib>
#include <cmath>
using namespace std;

#define MOD 10007
int n;
int dp[1005];

int main() {
    dp[0] = 1;
    dp[1] = 1;
    cin >> n;
    for(int i=2;i<=n;++i) {
        dp[i] = (dp[i - 2] + dp[i - 1]) % MOD;
    }
    cout << dp[n] << '\n';
    
    return 0;
}
