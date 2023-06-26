#include <iostream>
#include <cstdlib>
#include <cstdio>
#include <algorithm>
#include <vector>
#include <queue>
#include <cstring>
#include <string>
using namespace std;
typedef pair<int, int> pi;
int t;
int dp[15][15];
int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    
    cin >> t;
    for(int k=1;k<=t;++k) {
        int n;
        cin >> n;
        memset(dp, 0, sizeof(dp));
        dp[0][1] = 1;
        cout << '#' << k << endl;
        for(int i=1;i<=n;++i) {
            for(int j=1;j<=i;++j) {
                dp[i][j] = dp[i-1][j-1] + dp[i-1][j];
                cout << dp[i][j] << ' ';
            }
            cout << endl;
        }
    }
    
    return 0;
}
