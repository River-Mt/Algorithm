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
#define MAX 1e9
#define FIO ios_base::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);
int n, m, r;
int arr[305][305];

void print() {
    for(int i=0;i<n;++i) {
        for(int j=0;j<m;++j) {
            printf("%d ", arr[i][j]);
        }
        printf("\n");
    }
}

void counterClockRotate(int sr, int sc, int er, int ec) {
    int tmp = arr[sr][sc];
    for(int j = sc; j <= ec - 1; j++) {
        arr[sr][j] = arr[sr][j+1];
    }
    for(int i = sr; i <= er - 1; ++i) {
        arr[i][ec] = arr[i+1][ec];
    }
    for(int j = ec; j >= sc + 1; --j) {
        arr[er][j] = arr[er][j-1];
    }
    for(int i = er; i >= sc + 2; --i) {
        arr[i][sc] = arr[i-1][sc];
    }
    arr[sr+1][sc] = tmp;
    
}

int main() {
    scanf("%d %d %d", &n, &m, &r);
    
    for(int i=0;i<n;++i)
        for(int j=0;j<m;++j)
            scanf("%d", &arr[i][j]);
    
    int sr = 0, sc = 0;
    int er = n-1, ec = m-1;
    
    for(int i = 0; i<min(m,n)/2; ++i) {
        for(int j=0;j<r;++j) {
            counterClockRotate(sr, sc, er, ec);
        }
        sr += 1;
        sc += 1;
        er -= 1;
        ec -= 1;
    }
    
    print();
    
    return 0;
}
