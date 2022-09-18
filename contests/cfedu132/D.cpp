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

const int MAX_N = 2e5 + 2;
const int MAX_L = 18;

int n, m, q;
int arr[MAX_N], dp[MAX_N][MAX_L];

void build_sparse_table() {
    for (int i = 1; i <= m; i++)
        dp[i][0] = arr[i];
    for (int j = 1; j < MAX_L; j++)
        for (int i = 1; i + (1 << j) <= n + 1; i++)
            dp[i][j] = max(dp[i][j - 1], dp[i + (1 << (j - 1))][j - 1]);
}

int lg(int x) {
    return 32 - __builtin_clz(x) - 1;
}

int max_query(int l, int r) { // O(1)
    int k = lg(r - l + 1);
    return max(dp[l][k], dp[r - (1 << k) + 1][k]);
}

void solve() {
    cin >> n >> m;
    for (int i = 1; i <= m; i++) cin >> arr[i];

    build_sparse_table();
    // for (int i = 1; i <= 6; i++){
    //     for (int j = 0; j <= m; j++){
    //         cout << dp[j][i] << " ";
    //     }
    //     cout << endl;
    // }
    cin >> q;
    while (q--) {
        int x1, y1, x2, y2, k; cin >> x1 >> y1 >> x2 >> y2 >> k;
        int maxh = x1+k*(int)((n-x1)/k);
        cout << maxh << " " << max_query(y1, y2) << "\n";
        if (maxh <= max_query(y1, y2)) cout << "NO\n";
        else if ((maxh-x2) % k) cout << "NO\n";
        else if (abs(y2-y1)%k) cout << "NO\n";
        else cout << "YES\n";
    }
}

int main()
{
	ios_base::sync_with_stdio(0);
    cin.tie(0);
	int tc = 1;
    // cin >> tc;
	while(tc--){
		solve();
	}
	return 0;
}