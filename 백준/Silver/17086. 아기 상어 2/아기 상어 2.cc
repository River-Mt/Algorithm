#include <iostream>
#include <algorithm>
#include <vector>
#include <queue>
#include <stack>
#include <string>
#include <cmath>
using namespace std;
typedef pair<int, int> pi;
#define endl '\n'
#define MAX 55
#define FIO ios_base::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);

int n, m, ans;
int dr[] = {-1, -1, -1, 0, 0, 1, 1, 1};
int dc[] = {-1, 0, 1, -1, 1, -1, 0, 1};
int sea[MAX][MAX]; // 0 : empty, 1 : baby shark
int dist[MAX][MAX];
queue<pi> q;

void init() {
    FIO
    cin >> n >> m;
    for(int i = 0; i < n; i++) {
        for(int j = 0; j < m; j++) {
            cin >> sea[i][j];
            if(sea[i][j]) {
                dist[i][j] = 1;
                q.push({i, j});
            }
        }
    }
}

bool isOverRange(int r, int c) {
    if(r < 0 || c < 0 || r >= n || c >= m) return true;
    return false;
}

void bfs() {
    while(!q.empty()) {
        pi now = q.front();
        q.pop();
        ans = max(dist[now.first][now.second], ans);

        for(int d = 0; d < 8; d++) {
            int nr = now.first + dr[d];
            int nc = now.second + dc[d];
            if(isOverRange(nr, nc))continue;
            if(dist[nr][nc])continue;
            dist[nr][nc] = dist[now.first][now.second] + 1;
            q.push({nr, nc});
        }
    }
    
}

int main() {
    init();
    bfs();
    cout << ans - 1;
    return 0;
}
