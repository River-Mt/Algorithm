#include <iostream>
#include <cstdio>
#include <vector>
#include <stack>
#include <algorithm>
using namespace std;
#define x first
#define y second
typedef long long ll;
typedef pair<ll,ll> pii;
vector<pii>v;
int n;
int ccw(pii a,pii b,pii c){
    ll dir = (a.x*b.y+b.x*c.y+c.x*a.y)-(a.y*b.x+b.y*c.x+c.y*a.x);
    if(dir>0)return 1;
    else return dir<0?-1:0;
}

ll dist(pii a,pii b){
    return (b.x-a.x)*(b.x-a.x)+(b.y-a.y)*(b.y-a.y);
}

bool cmp1(pii a,pii b){
    if(a.x!=b.x)return a.x<b.x;
    return a.y<b.y;
}

bool cmp2(pii a,pii b){
    ll dir=ccw(v[0],a,b);
    return dir>0||(!dir&&(dist(v[0],a)<dist(v[0],b)));//반시계거나 같은직선에 위치한다면 거리순으로
}

int main(){
    scanf("%d",&n);
    v.resize(n);
    for(int i=0;i<n;++i)scanf("%lld %lld",&v[i].x,&v[i].y);
    sort(v.begin(),v.end(),cmp1);
    sort(v.begin()+1,v.end(),cmp2);

    stack<int>s;
    s.push(0); s.push(1);
    int nx=2;
    while(nx<n){
        while((int)s.size()>=2){
            int a,b;
            b=s.top(); s.pop();
            a=s.top();
            if(ccw(v[a],v[b],v[nx])>0){
                s.push(b);
                break;
            }
        }
        s.push(nx);
        nx++;
    }
    
    printf("%d",(int)s.size());
    

    return 0;
}
