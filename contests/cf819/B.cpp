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

template <class T>
void print_v(vector<T> &v) { cout << "{"; for (auto x : v) cout << x << ","; cout << "\b}"; }

#define MOD 1000000007
#define PI 3.1415926535897932384626433832795
string to_upper(string a) { for (int i=0;i<(int)a.size();++i) if (a[i]>='a' && a[i]<='z') a[i]-='a'-'A'; return a; }
string to_lower(string a) { for (int i=0;i<(int)a.size();++i) if (a[i]>='A' && a[i]<='Z') a[i]+='a'-'A'; return a; }
bool prime(ll a) { if (a==1) return 0; for (int i=2;i<=round(sqrt(a));++i) if (a%i==0) return 0; return 1; }

void solve() {
    int n, m;
    cin >> n >> m;
    if (n>m){
        cout << "No\n";
        return;
    }
    if ((m&1) && (n%2==0)){
        cout << "No\n";
        return;
    }
    cout << "Yes\n";
    if (n&1){
        for (int i=0;i<(n-1);i++) cout << "1 ";
        cout << (m-(n-1)) << endl;
        return;
    }
    for (int i=0;i<(n-2);i++) cout << "1 ";
    cout << ((m-(n-2))/2) << " " << ((m-(n-2))/2) << endl;
    return;
}

int main()
{
	ios_base::sync_with_stdio(0);
    cin.tie(0);
	int tc = 1;
	cin >> tc;
	while(tc--){
		solve();
	}
	return 0;
}