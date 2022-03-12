#include <iostream>
#include <vector>
#include <cmath>
using namespace std;

int ring(int a){
    if (a==1) return -1;
    return int((-1+pow(a-1,0.5))/2);
}

int excess(int a, int ring){
    return a-4*(ring*(ring+1))-2;
}

vector<int> pos(int e, int ring){
    vector<int> p = {-ring,-ring-1};
    if (e>(ring*2+1)){
        p[0]+=(ring*2+1);
        e-=(ring*2+1);
    }else{
        p[0]+=e;
        return p;
    }
    if (e>(ring*2+2)){
        p[1]+=(ring*2+2);
        e-=(ring*2+2);
    }else{
        p[1]+=e;
        return p;
    }
    if (e>ring*2+2){
        p[0]-=(ring*2+2);
        e-=(ring*2+2);
        p[1]-=e;
        return p;
    }else{
        p[0]-=e;
        return p;
    }
}

int main(){
    int a,b;
    cin >> a >> b;
    int ra = ring(a);
    int rb = ring(b);
    int ea = excess(a,ra);
    int eb = excess(b,rb);
    vector<int> pa = pos(ea,ra);
    vector<int> pb = pos(eb,rb);
    // cout << "ra: " << ra << " rb: " << rb << " ea: " << ea << " eb: " << eb << endl;
    cout << abs(pa[0]-pb[0])+abs(pa[1]-pb[1]);
}