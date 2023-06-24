#include <iostream>
#include <algorithm>
#include <vector>
#include <queue>
#include <string>
#include <cstdlib>
#include <cmath>
using namespace std;

#define MAX 100005

long long n, k, l, r, psum, cnt;
long long arr[MAX];

int main (){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    
    cin >> n;
    for(int i=0;i<n;++i) cin >> arr[i];
    cin >> k;
    
    while(r < n) {
        if(psum + arr[r] > k) {
            cnt += n - r;
            psum -= arr[l++];
        }
        else {
            psum += arr[r++];

        }
    }
    
    cout << cnt << endl;
    

    return 0;
}
