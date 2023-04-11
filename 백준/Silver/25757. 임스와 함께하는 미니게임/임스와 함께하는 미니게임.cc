#include <iostream>
#include <algorithm>
#include <vector>
#include <string>
#include <cctype>
#include <set>
#include <map>
using namespace std;
typedef pair<int, int> pi;
#define endl '\n'
#define MAX 10005
#define FIO ios_base::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);

int solve() {
    int n;
    char game;
    cin >> n >> game;
    
    map<char, int> mp;
    mp.insert({'Y', 1});
    mp.insert({'F', 2});
    mp.insert({'O', 3});

    set<string> st;
    
    for(int i = 0; i < n; i++) {
        string player;
        cin >> player;
        st.insert(player);
    }
    
    return (int)(st.size() / mp[game]);
    
}


int main() {
    FIO
    cout << solve() << endl;
    return 0;
}
