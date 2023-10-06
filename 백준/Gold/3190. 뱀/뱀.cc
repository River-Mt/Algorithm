#include <cstdio>
#include <iostream>
#include <algorithm>
#include <vector>
#include <queue>
#include <stack>
#include <map>
#include <set>
#include <string>
#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <deque>
using namespace std;
#define ll long long
#define pi pair<int,int>
#define ppi pair<int,pair<int,int>>
#define pll pair<ll,ll>
#define FOR(a,n) for(int i=a;i<n;++i)
#define FastIO ios_base::sync_with_stdio(false);cin.tie(NULL);cout.tie(NULL);
#define vvi vector<vector<int>>
#define vi vector<int>
#define vpi vector<pair<int,int>>
#define endl '\n'
#define INF 1000000
#define MOD 1000000000
#define MAX 1000005
#define all(v) v.begin(), v.end()
/*
 boj 3190 뱀
 
 초기상태 : loc = (1, 1), length = 1, dir = right
 
 매 초 마다 이동
 - 몸길이를 늘려 머리를 다음 칸에 위치
 - 이동한 칸에 사과가 있다면 그 칸에 사과가 없어지고 꼬리는 가만히
 - 이동한 칸에 사과가 없다면 몸 길이를 줄여 꼬리가 위치한 칸을 비워줌 (몸 길이 변화 X)
 
 todo : 뱀이 벽 또는 자기 자신의 몸과 부딪힐 때 까지의 초를 출력
 */
int n, k, l;
deque<pi>dq;
int dr[] = {0, 1, 0, -1};
int dc[] = {1, 0, -1, 0};
int chk[105][105], apple[105][105];
map<int, char>mp;

int main() {
    FastIO
    cin >> n >> k;
    
    for(int i = 0; i < k; ++i){
        int r, c;
        cin >> r >> c;
        apple[r][c] = 1;
    }
    
    cin >> l;
    
    for(int i = 0; i < l ; ++i){
        int sec;
        char ch;
        cin >> sec >> ch;
        mp[sec] = ch;
    }
    
    int cnt = 0;
    int dir = 0;
    bool flag = false;
    
    dq.push_back({1, 1}); // snake
    chk[1][1] = 1;

    while(true){
        cnt++;
        
        int hr = dq.front().first, hc = dq.front().second;
        int nr = hr + dr[dir], nc = hc + dc[dir];
        
        if(nr <= 0 || nc <= 0 || nr > n || nc > n || chk[nr][nc])break;
    
        dq.push_front({nr, nc});
        chk[nr][nc] = 1;
        
        if(apple[nr][nc] == 0){
            chk[dq.back().first][dq.back().second] = 0;
            dq.pop_back();
        }
        else apple[nr][nc] = 0;
        
        if(mp[cnt] == 'L')dir = (dir + 3) % 4;
        else if(mp[cnt] == 'D')dir = (dir + 1) % 4;
        
    }
    
    cout << cnt << endl;
    
    return 0;
}
