#include <vector>
#include <iostream>
#include <algorithm>
#include <numeric>
#include <functional>
using namespace std;

int main(){
    int n, q, t, x, y;
    cin >> n >> q;
    vector<int> price;
    for (int i=0; i<n ; i++){
        cin >> t;
        price.push_back(t);
    }
    sort(price.begin(), price.end(), greater<int>());

    for (int i=0; i<q; i++){
        cin >> x >> y;
        cout << accumulate(price.begin()+(x-y), price.begin()+x, 0);
    }
    return 0;
}