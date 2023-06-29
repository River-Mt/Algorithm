#include <iostream>
#include <queue>
#include <algorithm>
#include <vector>
using namespace std;
#define ll long long
int n, m;
vector<int>v;
int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);
    cin >> n >> m;
    v.resize(n);
    for(int i=0;i<n;++i)cin >> v[i];
    sort(v.begin(), v.end());
    for(int i=0;i<m;++i) {
        int s, e;
        cin >> s >> e;
      
        cout << upper_bound(v.begin(), v.end(), e) - lower_bound(v.begin(), v.end(), s) << '\n';
    }
     
    return 0;
}
         
