#include<cstdio>
#include<algorithm>
#include<queue>
#include<vector>
using namespace std;

int main() {
	vector<vector<int>>adj;
	vector<int>indegree, cost, ans;
	queue<int>q;
	int n;
	scanf("%d", &n);
	ans.resize(n+1),indegree.resize(n + 1), cost.resize(n + 1), adj.resize(n + 1);
	for (int i = 1; i <= n; i++) {
		int u;
		scanf("%d", &cost[i]);
		while (1) {
			scanf("%d", &u);
			if (u == -1)break;
			adj[u].push_back(i);
			indegree[i]++;
		}
	}
	for (int i = 1; i <= n; i++) {
		if (!indegree[i]) {
			q.push(i); ans[i] = cost[i];
		}
	}
	while (!q.empty()) {
		int cur = q.front();
		q.pop();
		for (auto&next : adj[cur]) {
			indegree[next]--;
			ans[next] = max(ans[next], ans[cur] + cost[next]);
			if (!indegree[next])q.push(next);
		}
	}
	for (int i = 1; i <= n; i++)printf("%d\n", ans[i]);
	return 0;
}