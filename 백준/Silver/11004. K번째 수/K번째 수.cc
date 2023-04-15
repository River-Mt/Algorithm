#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;
#define FIO ios_base::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);

int main() {
    FIO
    int n, k;
    cin >> n >> k;
    vector<int>v(n);
    for(int i = 0; i < n; i++)cin >> v[i];
    stable_sort(v.begin(), v.end());
    cout << v[k-1];
    return 0;
}
