#include<iostream>
#include<algorithm>
#include<vector>
#include<cstdio>
#include<string>
using namespace std;
vector<vector<int>>adj(32010);
vector<int>indegree(32010);
vector<int>ans;
bool chk[32010];

void dfs(int here) {
	chk[here] = 1;
	for (auto&x : adj[here]) {
		if (chk[x] == 0)dfs(x);
	}
	ans.push_back(here);
}


int main() {
	int n, m;
	cin >> n >> m;
	for (int i = 0; i < m; i++) {
		int a, b;
		cin >> a >> b;
		adj[a].push_back(b);
		indegree[b]++;
	}

	for (int i = 1; i <= n; i++) {
		if (!chk[i] && !indegree[i])dfs(i);
	}
	reverse(ans.begin(), ans.end());//dfs로 모든 정점을 순회하고 마지막의 정점에서부터 거꾸로 뒤집는다.
	for (int i = 0; i < n; i++) {
		cout << ans[i]<<' ';
	}




	return 0;
}