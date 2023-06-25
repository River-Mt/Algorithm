#include <iostream>
#include <algorithm>
#include <vector>
#include <queue>
#include <string>
#include <cstdlib>
#include <cmath>
using namespace std;

#define MOD 10007
int t;

int go(int cur) {
    if(cur == 1) return 1;
    if(cur == 2) return 2;
    if(cur == 3) return 4;
    
    return go(cur - 1) + go(cur - 2) + go(cur - 3);
        
}

int main() {
    ios_base::sync_with_stdio(false);cin.tie(NULL);cout.tie(NULL);
    cin >> t;
    while(t--) {
        int n;
        cin >> n;
        cout << go(n) << endl;
    }
    
    return 0;
}
