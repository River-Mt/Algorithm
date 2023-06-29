#include <iostream>
#include <queue>
#include <algorithm>
#include <vector>
using namespace std;
#define ll long long
int n, budget;
vector<int>v;
int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    cin >> n;
    v.resize(n);
    int l = 0;
    int r = 0;
    for(int i=0;i<n;++i){
        cin >> v[i];
        r = max(r, v[i]);
    }
    
    cin >> budget;
    
    while(l <= r) {
        int mid = (l + r) / 2, sum = 0;
        for(auto&money : v)
            sum += (money > mid) ? mid : money;
        if(sum > budget) r = mid - 1;
        else l = mid + 1;
    }
    
    cout << r;
     
    return 0;
}
         
