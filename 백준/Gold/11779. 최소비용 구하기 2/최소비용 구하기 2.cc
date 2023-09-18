#include<cstdio>
#include<vector>
#include<algorithm>
#include<queue>
#include<stack>
using namespace std;
typedef pair<int, int> P;
#define inf 1e9
vector<vector<P>> adj(1005);
priority_queue<P> pq;
vector<int> dist(1005, inf);
stack<int>out;
int trc[1005];
int n, m, a, b, city_cnt;
void dijk(int st) {
	pq.push({ st,0 });
	dist[st] = 0;
	while (!pq.empty()) {
		int now = pq.top().first, cost = -pq.top().second;
		pq.pop();
		if (dist[now] < cost) continue;
		for (auto& e : adj[now]) {
			int nv = e.first, nw = e.second;
			if (dist[nv] > cost + nw) {
				dist[nv] = cost + nw;
				trc[nv] = now;
				pq.push({ nv,-(cost + nw) });
			}
		}
	}

}

int main() {
	scanf("%d %d", &n, &m);
	for (int i = 0, x, y; i < m; i++) {
		int z;
		scanf("%d %d %d", &x, &y, &z);
		adj[x].push_back({ y, z });
	}
	scanf("%d%d", &a, &b);
	dijk(a);
	printf("%d\n", dist[b]);
	int t = b;
	while (t) {
		out.push(t);
		t = trc[t];
	}
	printf("%d\n", out.size());
	while (!out.empty()) {
		printf("%d ", out.top());
		out.pop();
	}
	return 0;
}

