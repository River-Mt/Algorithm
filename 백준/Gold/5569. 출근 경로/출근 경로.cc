#include <iostream>
#include <cstdio>
#include <algorithm>
#include <vector>
#include <cstring>
using namespace std;
#define MOD 100000
int w, h;
// 동쪽, 북쪽으로만 이동 가능
// 연속 두 번 방향을 바꿀 수는 없음
// [r][c][dir]
int dp[105][105][2][2];

int getDP(int r, int c, int p, int d) {
    if(r > h || c > w) return 0;
    if(r == h && c == w) return 1;
    int&ret = dp[r][c][p][d];
    if(ret != -1) return ret;
    if(d == 0) {
        ret = getDP(r + 1, c, 0, 0);
        if(!p) ret = (ret + getDP(r, c + 1, 1, 1)) % MOD;
    }
    else {
        ret = getDP(r, c + 1, 0, 1);
        if(!p) ret = (ret + getDP(r + 1, c, 1, 0)) % MOD;
    }
    return ret;
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);
    cin >> w >> h;
    memset(dp, -1, sizeof(dp));
    cout << (getDP(2, 1, 0, 0) + getDP(1, 2, 0, 1)) % MOD;
 
    return 0;
}
