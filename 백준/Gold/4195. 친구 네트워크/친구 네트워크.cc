#include<iostream>
#include<cstdio>
#include<map>
#include<algorithm>
#include<unordered_map>
#include<string>
#include<vector>
using namespace std;
unordered_map<string, int>um;//기존의맵은 레드블랙트리인데 애는 해시테이블을 사용해서 탐색이 더빠르다
int p[200005], cnt[200005],fr=1;
vector<int>ans;
int find(int x) {
	return(x == p[x]) ? x : p[x] = find(p[x]);
}

int merge(int n, int m) {
	n = find(n); m = find(m);
	if (n == m)return cnt[m];
	p[n] = m; cnt[m] += cnt[n]; cnt[n] = 1;	
	return cnt[m];
}

int main() {
	ios_base::sync_with_stdio(false); cin.tie(0);
	int t,f;
	cin >> t;
	while (t--) {
		cin >> f;
		for (int i = 1; i <= f * 2; i++) { 
			p[i] = i; 
			cnt[i] = 1; 
		}
		string a, b;

		for (int i = 0; i <f; i++) {
			cin >> a >> b;
			if (!(um.count(a)))um[a] = fr++;
			if (!(um.count(b)))um[b] = fr++;
			ans.push_back(merge(um[a], um[b]));
		}
		
	}
	for (auto&x : ans)printf("%d\n", x);



	return 0;
}