#include <bits/stdc++.h>
using namespace std;

int count(vector<string>& v, char ch) {
    int cnt = 0;
    for(int i=0;i<3;++i){
        for(int j=0;j<3;++j) {
            if(v[i][j] == ch) cnt += 1;
        }
    }
    return cnt;
}

bool who_is_win(vector<string>& v, char ch) {
    for(int i=0;i<3;++i) {
        if (v[i][0] == ch && v[i][1] == ch && v[i][1] == ch && v[i][2] == ch) return true;
        if (v[0][i] == ch && v[1][i] == ch && v[1][i] == ch && v[2][i] == ch) return true;
    }
    
    if (v[0][0] == ch && v[1][1] == ch && v[1][1] == ch && v[2][2] == ch) return true;
    if (v[0][2] == ch && v[1][1] == ch && v[1][1] == ch && v[2][0] == ch) return true;
    
    return false;
}

int solution(vector<string> board) {
    int answer = -1;
    int cnt_o = count(board, 'O');
    int cnt_x = count(board, 'X');
    
    if(abs(cnt_o - cnt_x) > 1 or cnt_o < cnt_x) return 0;
    else if(who_is_win(board, 'O') and cnt_o - cnt_x != 1) return 0;
    else if(who_is_win(board, 'X') and cnt_x - cnt_o != 0) return 0;
    else if (who_is_win(board, 'O') and who_is_win(board, 'X')) return 0;

    return 1;
}