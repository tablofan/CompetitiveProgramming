#include <bits/stdc++.h>
using namespace std;
#define ll long long
#define vi vector<int>
#define vll vector<long long>
#define mii map<int, int>
#define f(i,s,e) for(long long int i=s;i<e;i++)
#define cf(i,s,e) for(long long int i=s;i<=e;i++)
#define rf(i,e,s) for(long long int i=e-1;i>=s;i--)
#define pb push_back


void solve() {
    int n, temp;
    cin >> n;
    vi a;
    vi b;
    for (int i=0;i<n;i++){
        cin >> temp;
        a.pb(temp);
    }
    for (int i=0;i<n;i++){
        cin >> temp;
        b.pb(temp);
    }
    a.pb(a[0]);
    b.pb(b[0]);
    for (int i=0;i<a.size();i++){
        if (a[i]>b[i]){
            cout << "NO\n";
            return;
        }
    }
    for (int i=0;i<b.size()-1;i++){
        if (b[i]>b[i+1]+1 && b[i]!=a[i]){
            cout << "NO\n";
            return;
        }
    }
    cout << "YES\n";
    return;
}

int main()
{
	ios_base::sync_with_stdio(0);
    cin.tie(0);
	int tc;
	cin >> tc;
	while(tc--){
		solve();
	}
	return 0;
}
