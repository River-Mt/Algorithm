#include <iostream>
#include <string>
using namespace std;
string S;
int chk[4];
int main(){
    ios_base::sync_with_stdio(0); cin.tie(0); cout.tie(0);
    cin>>S;
    int sz = (int)S.size();
    for(int i=0;i<sz;++i){
        if(S[i]=='A')chk[0]++;
        else if(S[i]=='B')chk[1]++;
        else if(S[i]=='C')chk[2]++;
    }
    if(chk[0]){
        for(int i=0;i<sz;++i){
            if(S[i]=='B'||S[i]=='C'||S[i]=='D'||S[i]=='F')cout<<'A';
            else cout<<S[i];
        }
    }
    else if(chk[1]){
        for(int i=0;i<sz;++i){
            if(S[i]=='C'||S[i]=='D'||S[i]=='F')cout<<'B';
            else cout<<S[i];
        }
    }
    else if(chk[2]){
        for(int i=0;i<sz;++i){
            if(S[i]=='D'||S[i]=='F')cout<<'C';
            else cout<<S[i];
        }
    }
    
    else {
        while(sz--)cout<<'A';
    }
    
    return 0;
}
