#include<stdio.h>
int arr[1005];
int dp[1005];
int max;

int main() {
	int n;
	scanf("%d", &n);

	for (int i = 1; i <= n; i++) {
		scanf("%d", &arr[i]);
	}
	
	for (int i = 1; i <= n; i++) {
		dp[i] = arr[i];
		for (int j = 0; j < i; j++) {
			if (arr[j] < arr[i]) {
				if (dp[i] < dp[j] +arr[i]) {
					dp[i] = dp[j] + arr[i];
				}
			}
			if (max < dp[i])max = dp[i];
		}
	}

	printf("%d", max);

	return 0;
}