#include <iostream>
#include <vector>
#include <unordered_set>
using namespace std;

int main(){
    int t;
    cin >> t;
    for (int c=0;c<t;c++){
        int n;
        unordered_set<int> s;
        vector<int> res;
        cin >> n;
        for (int i=1;i<n+1;i++){
            if (i*2>n) break;
            if (s.find(i) == s.end()){
                s.insert(i);
                s.insert(i*2);
                res.push_back(i);
                res.push_back(i*2);
            }
        }
        cout << "2\n";
        for (int i=1;i<n+1;i++){
            if (s.find(i) == s.end()) res.push_back(i);
        }
        for (auto i: res) cout << i << ' ';
        cout << "\n";
    }
}