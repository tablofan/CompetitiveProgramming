#include <bits/stdc++.h>
using namespace std;

void solve() {
    vector<string> m = {"42101", "22100", "22101"};
    int height = m.size();
    int width = m[0].size();
    int res = 1;
    for (int size=1;size<min(height, width);size++)
        for (int i=0;i+size<height;i++)
            for (int j=0;j+size<width;j++)
                if (m[i][j] == m[i][j+size] and m[i][j+size] == m[i+size][j] and m[i+size][j] == m[i+size][j+size])
                    res = (size+1)*(size+1);
    cout << res << endl;
}

int main()
{
    solve();
	return 0;
}