#include <cstdio>
#include <algorithm>
#include <iostream>
#include <queue>
#include <vector>
using namespace std;
#define ll long long
int n;
ll ans1,ans2,ans3;
vector<int>hon,psum;
int main(){
    cin>>n;
    hon.resize(n+1),psum.resize(n+1);
    for(int i=1;i<=n;++i){
        cin>>hon[i];
        psum[i]=psum[i-1]+hon[i];
    }
    
    for(int i=2;i<n;++i){
        ans1=max(ans1,(ll)(psum[n]-hon[1]-hon[i]+psum[n]-psum[i]));
        ans2=max(ans2,(ll)(psum[n]-hon[n]-hon[i]+psum[i-1]));
        ans3=max(ans3,(ll)(psum[i]-hon[1]+psum[n]-psum[i-1]-hon[n]));
    }
    
    cout<<max({ans1,ans2,ans3});
    return 0;
}

