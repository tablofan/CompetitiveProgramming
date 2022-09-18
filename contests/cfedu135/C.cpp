#include <bits/stdc++.h>
using namespace std;
#define ll long long
#define vi vector<int>
#define pb push_back
#define MOD 1000000007
#define PI 3.1415926535897932384626433832795

void solve(){
    int n;
    cin >> n;
    // cout << n << "\n";
    multiset<int> a, b, c;
    vi ta;
    int temp;
    int res = 0;
    for (int i=0;i<n;i++){
        cin >> temp;
        a.insert(temp);
    }
    for (int i=0;i<n;i++){
        cin >> temp;
        b.insert(temp);
    }
    // cout << "c3\n";
    set_intersection(a.begin(), a.end(), b.begin(), b.end(), inserter(c, c.begin()));
    // cout << "c4\n";
    for(int elem : c) {
        a.erase(elem);
        b.erase(elem);
        cout << elem << ' ';
    } 
    cout << "\n";
    // cout << "c1\n";
    for (auto &i:a){
        if (i>9){
            temp = int(to_string(i).size());
            res++;
            ta.pb(i);
            a.insert(temp);
        }
    }
    for (int i:ta) a.erase(a.lower_bound(i));
    ta.clear();
    for (auto &i:b){
        if (i>9){
            temp = to_string(i).size();
            res++;
            ta.pb(i);
            b.insert(temp);
        }
    }
    for (int i:ta) b.erase(b.lower_bound(i));
    ta.clear();
    cout << "c2\n";
    for (int i:a) cout << i << ' ';
    cout << "\n";
    for (int i:b) cout << i << ' ';
    cout << "\n";
    c.clear();
    set_intersection(a.begin(), a.end(), b.begin(), b.end(), inserter(c, c.begin()));
    for(int i : c) {
        a.erase(a.lower_bound(i));
        b.erase(b.lower_bound(i));
        cout << i << ' ';
    }
    cout << endl;
    for (int i:a) cout << i << ' ';
    cout << "\n";
    for (int i:b) cout << i << ' ';
    cout << "\n";
    for (auto &i:a) if (i>1) res++;
    for (auto &i:b) if (i>1) res++;
    cout << res << endl;
}

int main(){
	// ios_base::sync_with_stdio(0);
    // cin.tie(0);
	int tc;
	cin >> tc; //comment out if 1 case
	while(tc--)
		solve();
	return 0;
}