#include <iostream>
#include <algorithm>
#include <vector>
#include <queue>
#include <string>
#include <cstdlib>
#include <cmath>
using namespace std;

int n, m;
int chk[105][105];
int dr[] = {0, 0, -1, 1};
int dc[] = {-1, 1, 0, 0};

vector<string>board;
typedef pair<int, int> pi;

bool isOver(int r, int c) {
    if(r < 0 || c < 0 || r >= n || c >= m) return true;
    else return false;
}

int dfs(int r, int c, char color) {
    chk[r][c] = 1;
    int ret = 1;
    for(int d=0;d<4;++d) {
        int nr = r + dr[d];
        int nc = c + dc[d];
        if(isOver(nr, nc) || board[nr][nc] != color || chk[nr][nc]) continue;
        ret += dfs(nr, nc, color);
    }
    return ret;
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    
    cin >> m >> n;
    
    for(int i=0;i<n;++i) {
        string line;
        cin >> line;
        board.push_back(line);
    }
    
    int wsum = 0;
    int bsum = 0;
    
    for(int i=0;i<n;++i) {
        for(int j=0;j<m;++j) {
            if(chk[i][j]) continue;
            
            if(board[i][j] == 'W'){
                int tmp = dfs(i, j, 'W');
                wsum += tmp * tmp;
            }
            else {
                int tmp = dfs(i, j, 'B');
                bsum += tmp * tmp;
            }
        }
    }
    
    cout << wsum << ' ' << bsum << '\n';

    return 0;
}
