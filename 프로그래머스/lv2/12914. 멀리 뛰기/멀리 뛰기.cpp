#include <string>
#include <vector>

using namespace std;
#define MAX 2005
#define MOD 1234567

long long dp[MAX];


long long solution(int n) {
    long long answer = 0;
    dp[1] = 1;
    dp[2] = 2;
    
    for(int i=3;i<=n;++i) {
        dp[i] = (dp[i-1] + dp[i-2])%MOD;
    }

    return answer = dp[n];
}