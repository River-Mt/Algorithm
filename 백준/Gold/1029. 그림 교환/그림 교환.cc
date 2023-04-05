#include<cstdio>
#include<algorithm>
#include<vector>
#include<queue>
using namespace std;
int cost[20][20],n;
int dp[20][15][1<<16];//[현재 파는사람][가격][상태(visit)]
int paint_change(int state,int artist,int cos,int passed) {
	int&ret = dp[artist][cos][state];
	if (ret)return ret;
	ret =passed;
	for (int i = 0; i < n; i++) {
		if (state&(1 << i) || cost[artist][i] < cos)continue;//방문했거나 내가 산 가격보다 팔가격이 작으면 continue! 
		ret=max(ret,paint_change(state | (1 << i), i, cost[artist][i],passed+1));
	}
	return ret;
}

int main() {
	scanf("%d", &n);
	for (int i = 0; i < n; i++)for (int j = 0; j < n; j++)scanf("%1d", &cost[i][j]);
	printf("%d", paint_change(1, 0, 0,1));

	return 0;
}