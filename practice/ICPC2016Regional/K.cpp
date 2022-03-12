#include <iostream>
#include <unordered_map>
#include <algorithm>
using namespace std;

int main(){
    string s;
    cin >> s;
    transform(s.begin(), s.end(), s.begin(), ::toupper);
    unordered_map<char,int> c1, c2;
    for (auto &i:"KANGAROO") c1[i] += 1;
    for (auto &i:"KIWIBIRD") c2[i] += 1;
    int r1 = 0, r2 = 0;
    for (auto &i:s){
        r1 += c1[i];
        r2 += c2[i];
    }
    if (r1 > r2) cout << "Kangaroos";
    else if(r2 > r1) cout << "Kiwis";
    else cout << "Feud continues";
    return 0;
}