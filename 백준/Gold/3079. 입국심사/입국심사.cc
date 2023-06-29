#include <iostream>
#include <queue>
#include <algorithm>
#include <vector>
using namespace std;
#define ll long long
int n, m;
vector<ll> v;
int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);
    cin >> n >> m;
    v.resize(n);
    for(int i=0;i<n;++i) cin >> v[i];
    sort(v.begin(), v.end());
    
    ll l = 0, r = v[0] * (ll)m;
    ll ans = r;
    
    while(l <= r) {
        ll mid = (l + r) / 2;
        ll cnt = 0;
        for(auto&t : v) cnt += mid / t;
        if (cnt >= m) {
            ans = min(mid, ans);
            r = mid - 1;
        }
        else l = mid + 1;
    }
    cout << ans;

    return 0;
}
         
