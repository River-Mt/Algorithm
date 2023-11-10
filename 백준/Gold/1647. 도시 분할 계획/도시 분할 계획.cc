#include <iostream>
#include <cstdio>
#include <queue>
#include <vector>
#include <algorithm>
#include <cmath>
using namespace std;
#define ll long long
struct Edge{int cost,u,v;};
vector<int>pa,gp_size;
vector<Edge>eg;
int N,M,sz;
void myHeapify(int idx){//edge m개를 힙으로 O(m)으로 구현
    int lc = 2*idx+1,rc=2*idx+2,s=idx;
    if(lc<sz&&eg[lc].cost<eg[idx].cost)s=lc;
    if(rc<sz&&eg[rc].cost<eg[s].cost)s=rc;
    if(s!=idx){
        swap(eg[idx],eg[s]);
        myHeapify(s);
    }
}

Edge myDeleteMin(){//루트삭제, 마지막노드를 루트로 바꾸고 자식과 비교하며 swap하여 힙 유지
    sz--;
    Edge ret =eg[0];
    eg[0] = eg[sz];
    myHeapify(0);
    return ret;
}

int myFind(int x){//경로압축
    return (pa[x]==x)?x:pa[x]=myFind(pa[x]);
}

void myUnion(int a,int b){//가중경로
    //a=myFind(a); b=myFind(b);
    if(a==b)return;
    if(gp_size[a]<gp_size[b])swap(a,b);
    gp_size[a]+=gp_size[b];
    pa[b]=a;
}

void readGraph(){
    scanf("%d %d",&N,&M);
    pa.resize(N);
    gp_size.resize(N);
    sz=M;
    for(int i=0;i<N;++i){
        pa[i]=i;
        gp_size[i]=1;
    }
    for(int i=0;i<M;++i){
        int u,v,c;
        scanf("%d %d %d",&u,&v,&c);
        eg.push_back({c,u-1,v-1});
    }
}
int main(){
    readGraph();
    for(int i=sz/2-1;i>=0;i--)myHeapify(i);
    ll ans=0;
    int tmp=0;
    for(int i=0;i<M;++i){
        Edge root = myDeleteMin();
        int a = myFind(root.u);
        int b = myFind(root.v);
        if(a==b)continue;
        myUnion(a,b);
        ans+=(ll)root.cost;
        tmp=max(tmp,root.cost);
    }
    printf("%lld",ans-tmp);
    return 0;
}
