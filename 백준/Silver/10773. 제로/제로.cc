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
#include <regex>
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
#define INF 1e9
#define MOD 1000000000
#define MAX 25
#define all(v) v.begin(), v.end()
#define compress(v) v.erase(unique(all(v)),v.end());

int k, sum;
stack<int> st;

int main(){
    FastIO
    cin >> k;
    for(int i = 0; i < k; i++) {
        int num ;
        cin >> num;
    
        !num ? st.pop() : st.push(num);
    }
    
    while(!st.empty()) {
        sum += st.top();
        st.pop();
    }
    
    cout << sum << endl;
    
    return 0;
}
