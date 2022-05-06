#include <iostream>
#include <queue>
#include <vector>
#include <utility>
#include <tuple>
#include <string.h>
#define intmax 2147483647
#define llmax 9000000000000000
#define ll long long
using namespace std;

const int m = 100005;
ll v[m], d1[m], d2[m];

void djikstra(ll s, ll* d, vector<vector<pair<ll, ll>>> &g){
    priority_queue<pair<ll, ll>> q;
    for (int i=1; i<m; i++) d[i] = llmax;
    d[s] = 0;
    q.push({0,s});
    memset(v, 0, sizeof v);
    while (!q.empty()){
        ll a = q.top().second;
        q.pop();
        if (v[a]) continue;
        v[a]++;
        for (auto &[b, dist]: g[a]){
            if (d[a]+dist < d[b]){
                d[b] = d[a] + dist;
                q.push({-d[b], b});
            }
        }
    }
}

int main(){
    int n, m;
    cin >> n >> m;
    vector<vector<pair<ll, ll>>> g1(n+1), g2(n+1);
    vector<tuple<ll, ll, ll>> e;
    for (int i=0; i<m; i++){
        int a, b, dist;
        cin >> a >> b >> dist;
        e.push_back({a, b, dist});
        g1[a].push_back({b, dist});
        g2[b].push_back({a, dist});
    }
    djikstra(1, d1, g1);
    djikstra(n, d2, g2);
    ll res = llmax;
    for (auto &[a, b, dist]: e) res = min(res, d1[a]+d2[b]+dist/2);
    cout << res;
    return 0;
}