#include <iostream>
#include <unordered_set>
#include <vector>
using namespace std;
unordered_set<pair<int, int>> cache;
int rec(int start, int end, int summ, int moves){
    if ()
}   

void solve(){
    int n, s, sum;
    cin >> n >> s;
    vector<int> arr;
    for (int i=0; i<n; i++){
        int temp;
        cin >> temp;
        if (temp==1) sum += 1;
        arr.push_back(temp);
    }
    rec(0, n-1, sum, 0);
}

int main(){
    int tests;
    cin >> tests;
    for (int i = 0; i<tests;i++){

    }
    return 0;
}