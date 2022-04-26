#include <iostream>
using namespace std;

const int N = 100005;
int seg[N*3];
int lazy[N*3];

void up(int curr){
    seg[curr] = seg[curr<<1] + seg[curr<<1|1];
    return;
}

void down(int curr, int length){
    if (lazy[curr]){
        lazy[curr<<1] ^= 1;
        lazy[curr<<1|1] ^= 1;
        seg[curr<<1] = length-(length>>1)-seg[curr<<1];
        seg[curr<<1|1] = (length>>1)-seg[curr<<1|1];
        lazy[curr] = 0;
    }
    return;
}

void update(int start, int end, int l, int r, int curr){
    if (start <= l && end >= r){
        seg[curr] = r-l+1-seg[curr];
        lazy[curr] ^= 1;
        return;
    }
    down(curr, r-l+1);
    int mid = (l+r)/2;
    if (start <= mid) update(start, end, l, mid, curr<<1);
    if (end > mid) update(start, end, mid+1, r, curr<<1|1);
    up(curr);
    return;
}

int query(int start, int end, int l, int r, int curr){
    if (start <= l && end >= r) return seg[curr];
    down(curr, r-l+1);
    int mid = (l+r)/2;
    int res = 0;
    if (start <= mid) res += query(start, end, l, mid, curr << 1);
    if (end > mid) res += query(start, end, mid+1, r, curr << 1 | 1);
    return res;
}

int main(){
    int n, m, t, start, end;
    cin >> n >> m;
    for (int i=0;i<m;i++){
        cin >> t >> start >> end;
        if (!t) update(start, end, 1, n, 1);
        else{
            cout << query(start, end, 1, n, 1) << endl;
        }
    }
    return 0;
}