#include <vector>
#include <iostream>
using namespace std;

int n,h,v,w,nearest;
vector<int> tree;

void update(int node, int nodelow, int nodehigh, int updatelow, int updatehigh){
    if(updatelow <= nodelow && updatehigh >= nodehigh){
        tree[node] = 1;
        return;
    }
    if(nodehigh < updatelow || nodelow > updatehigh)return;
    int lastinleft = (nodelow + nodehigh)/2;
    update(2*node, nodelow, lastinleft, updatelow, updatehigh);
    update(2*node+1, lastinleft+1, nodehigh, updatelow, updatehigh);
    return;
}

bool query(int root){
    if(tree[root] == 1)return(true);
    if(root>nearest)return(false);
    return(query(root*2) && query(root*2+1));
}


int main(){
    cin>>n>>h>>v>>w;
    if(v*w >= h){
        cout<<"GAME OVER";
        return 0;
    }
    for(int i=0;i<h;i++){
        tree.push_back(0);
    }
    nearest = h;
    while(__builtin_popcount(nearest) != 1){
        tree.push_back(0);
        nearest++;
    }
    tree.resize(2*nearest);
    update(1,0,nearest-1,h,nearest-1);
    int c,r,start,end;
    for(int i=0;i<n;i++){
        cin>>c>>r;
        start = (r+c*v)%h;
        end = (start+w*v)%h;
        if(start>end){
            update(1,0,nearest-1,start,h-1);
            update(1,0,nearest-1,0,end);
        }
        else{
            update(1,0,nearest-1,start,end);
        }
    }
    string res = (query(1))?"GAME OVER":"VICTORY";
    cout<<res<<endl;
    return 0;
}