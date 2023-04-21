#include<vector>
#include<algorithm>
#include<queue>
#include<stack>
using namespace std;

int bfs(vector<vector<int>>& maps) {
    queue<pair<int, int>>q;
    int n = maps.size();
    int m = maps[0].size();
    int dist[105][105] = {0, };
    int dr[] = {0,0,-1,1};
    int dc[] = {-1,1,0,0};
    q.push({0, 0});
    dist[0][0] = 1;
    
    while(!q.empty()) {
        int r = q.front().first;
        int c = q.front().second;
        q.pop();
        if(r == n - 1 && c == m - 1) return dist[r][c];
        for(int i=0;i<4;++i) {
            int nr = r + dr[i];
            int nc = c + dc[i];
            if(nr < 0 || nc < 0 || nr >= n || nc >= m || dist[nr][nc] || maps[nr][nc] == 0)continue;
            q.push({nr, nc});
            dist[nr][nc] = dist[r][c] + 1;
            
        }
        
    }
    return -1;
}

int solution(vector<vector<int> > maps)
{
    int answer = 0;
    return answer = bfs(maps);
}