#include<iostream>
#include<algorithm>

using namespace std;

int coin[101];
int dp[100001];
int n, k;

int main() {
	cin >> n >> k;

	dp[0] = 1;

	for (int i = 0; i < n; i++)
		cin >> coin[i];

	for (int i = 0; i < n; i++) {
		for (int j = coin[i]; j <= k; j++)
			dp[j] += dp[j - coin[i]];
	}

	printf("%d", dp[k]);

	return 0;

}