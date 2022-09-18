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
    int n;
    cin >> n;
    string inp;
    cin >> inp;
    vi p;
    for (int i=0; i<n;i++){
        p.pb(-1);
        p.pb(-1);
    }
    int minus = 0;
    vi stack;
    for (int i=0;i<2*n;i++){
        if (inp[i] == '('){
            stack.pb(i);
            if (i-1>=0 && inp[i-1]==')') p[i] = p[i-1];
        }
        else{
            p[i] = stack.back();
            stack.pop_back();
        }
    }
    int r = 0;
    for (auto &i:p){
        if (i==-1) r += 1;
    }
    cout << r << endl;
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