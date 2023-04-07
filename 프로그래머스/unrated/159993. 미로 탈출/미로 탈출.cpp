#include <string>
#include <vector>
#include <algorithm>
#include <queue>
#include <stack>
#include <iostream>
using namespace std;
typedef pair<int,int> pi;
int sr, sc, lr, lc, er, ec;
int maps_row, maps_col;
int dr[] = {0,0,-1,1}, dc[] = {-1,1,0,0};

bool isOverRange(int r, int c) {
    if(r < 0 || c < 0 || r >= maps_row || c >= maps_col)return true;
    return false;
}

bool isWall(char ch) {
    if(ch == 'X')return true;
    return false;
}

int bfs(int fr, int fc, int tr, int tc, vector<string> maps) {
    queue<pair<pi, int>> q;
    int chk[105][105] = {0, };

    q.push({{fr, fc}, 0});
    
    while(!q.empty()) {
        pair<pi,int> now = q.front();
        int r = now.first.first;
        int c = now.first.second;
        int d = now.second;
        q.pop();
        
        if(r == tr && c == tc) return d;
        
        for(int i=0;i<4;++i) {
            int nr = r + dr[i];
            int nc = c + dc[i];
            if(isOverRange(nr, nc) || chk[nr][nc] ||isWall(maps[nr][nc]))continue;
            q.push({{nr, nc}, d + 1});
            chk[nr][nc] = 1;
        }
    }
    return 0;
}

int solution(vector<string> maps) {
    int answer = 0;
    maps_row = maps.size();
    maps_col = maps[0].size();
    
    for(int i=0;i<maps_row;++i) {
        for(int j=0;j<maps_col;++j) {
            if(maps[i][j] == 'S') {
                sr = i;
                sc = j;
            }
            if(maps[i][j] == 'L') {
                lr = i;
                lc = j;
            }
            if(maps[i][j] == 'E') {
                er = i;
                ec = j;
            }
        }
    }
    
    int stol = bfs(sr, sc, lr, lc, maps);
    int ltoe = bfs(lr, lc, er, ec, maps);
    
    return answer = (stol * ltoe) ? stol + ltoe : -1;
}