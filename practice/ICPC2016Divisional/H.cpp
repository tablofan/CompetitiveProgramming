#include <vector>
#include <unordered_map>
#include <iostream>
// #include <chrono>
#include <map>
using namespace std;
// using namespace std::chrono;

const int k = 100;

vector<vector<unordered_map<int, double>>> dp(81, vector<unordered_map<int, double>>(81));
double dfs(int l, int r, int t) {
    if (l > r || t<k) return 0;
    if (dp[l][r].count(t))
        return dp[l][r][t];
    double ans = 0;
    for (int i = l; i <= r; ++i) {
        auto accept = max(dfs(i, r, t - 2 * k), (double)i);
        auto reject = dfs(l, i - 1, t - k);
        double ev = (accept*(r-i+1)+reject*(i-l))/(r-l+1);
        ans = max(ans, ev);
    }
    return dp[l][r][t] = ans;
}

int main() {
    int l, r, t;
    cin >> l >> r >> t;
    // auto start = high_resolution_clock::now();
    cout << fixed;
    cout << dfs(l, r, t) << endl;
    // auto stop = high_resolution_clock::now();
    // auto duration = duration_cast<milliseconds>(stop - start);
    // cout << "Time: " << duration.count() << endl;
    return 0;
}