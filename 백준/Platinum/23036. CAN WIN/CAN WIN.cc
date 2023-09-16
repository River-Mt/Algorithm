#include <cstdio>
#include <algorithm>
#include <vector>
#include <iostream>
using namespace std;
#define ll long long
#define MAX 1000005
ll tree[MAX], n, arr[MAX], p, ans;
vector<ll> comp;

void make_comp(){
    for(int i=1; i<=n; i++) {
        cin >> arr[i];
        arr[i] += arr[i-1];
    }
    
    for(int i=0; i<=n; i++) {
        arr[i] -= p*i;
        comp.push_back(arr[i]);
    }
}

void compress(){
    sort(comp.begin(),comp.end());
    comp.erase(unique(comp.begin(),comp.end()),comp.end());
    for(int i=0; i<=n; i++)arr[i] = lower_bound(comp.begin(),comp.end(),arr[i])-comp.begin()+1;
}

void update(ll x){
    for(x++; x<MAX; x+=x&-x)tree[x]++;
}

ll query(ll x){
    ll ret = 0;
    for(x++; x; x-=x&-x)ret += tree[x];
    return ret;
}


int main(){
    ios_base::sync_with_stdio(0); cin.tie(0); cout.tie(0);
    cin >> n >> p;
    
    make_comp();
    compress();
 
    for(int i=0; i<=n; i++) {
        ll xx =query(arr[i]);
        ans += xx;
        update(arr[i]);
    }

    cout << ans;
}
