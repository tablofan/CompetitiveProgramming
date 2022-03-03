#include <iostream>
#include <vector>
#include <algorithm>
#include <map>
#include <unordered_map>
using namespace std;

struct suffix{
    int index;
    pair<int,int> rank;
    suffix(int a, int b, int c){
        index = a;
        rank = {b,c};
    }
};

vector<int> buildSuffix(string txt, int n){
    vector<suffix> s;
    for (int i=0;i<n;i++){
        int rank0 = txt[i]-'A';
        int rank1 = (i+1<n) ? txt[i+1]-'A' : -1;
        suffix temp(i, rank0, rank1);
        s.push_back(temp);
    }
    sort(s.begin(),s.end(), [](const suffix &x, const suffix &y){ return (x.rank < y.rank);});
    vector<int> ind(n,0);
    int k = 4;
    while (k<2*n){
        int rank = 0;
        int prev_rank = s[0].rank.first;
        s[0].rank.first = rank;
        ind[s[0].index] = 0;
        for (int i=1;i<n;i++){
            if (s[i].rank.first == prev_rank && s[i].rank.second == s[i-1].rank.second){
                prev_rank = s[i].rank.first;
                s[i].rank.first = rank;
            }
            else{
                prev_rank = s[i].rank.first;
                rank += 1;
                s[i].rank.first = rank;
            }
            ind[s[i].index] = i;
        }
        int nextindex;
        for (int i=0;i<n;i++){
            nextindex = s[i].index + k/2;
            s[i].rank.second = (nextindex<n)?s[ind[nextindex]].rank.first:-1;
        }
        sort(s.begin(),s.end(), [](const suffix &x, const suffix &y){ return (x.rank < y.rank);});
        k *= 2;
    }
    vector<int> res(n,0);
    for (int i=0;i<n;i++){
        res[i] = s[i].index;
    }
    return res;
}

vector<int> buildLCP(string t, vector<int> suf){
    int n = suf.size();
    vector<int> inv(n,0);
    vector<int> lcp(n,0);
    for (int i=0;i<n;i++){
        inv[suf[i]] = i;
    }
    int k = 0;
    int j;
    for (int i=0;i<n;i++){
        if (inv[i] == n-1){
            k=0;
            continue;
        }
        j = suf[inv[i]+1];
        while (i+k<n && j+k<n && (t[i+k]==t[j+k])){
            k += 1;
        }
        lcp[inv[i]] = k;
        if (k>0){
            k -= 1;
        }
    }
    return lcp;
}

int dp(vector<int>& s, vector<int>& e, vector<int>& l) {
    map<int, int> times;
    unordered_map<int, vector<pair<int, int>>> j;
    for (auto i = 0; i < s.size(); ++i) {
        times[s[i]] = 0;
        j[s[i]].push_back({e[i],l[i]});
    }    
    int res = 0;
    for (auto it = rbegin(times); it != rend(times); ++it) {
        for (auto i : j[it->first]) {
            auto it = times.lower_bound(i.first);
            res = max(res, (it == end(times) ? 0 : it->second) + i.second);
        }
        it->second = res;
    }
    return res;
}  

int main(){
    string s1,s2;
    cin >> s1 >> s2;
    string t = s1 + '#' + s2 + '$';
    int len1 = s1.length();
    vector<int> suf = buildSuffix(t,t.length());
    vector<int> lcp = buildLCP(t, suf);
    vector<int> s;
    vector<int> e;
    vector<int> l;
    for (int i=0;i<suf.size();i++){
        cout << suf[i] << " ";
    }
    cout << "\n";
    for (int i=0;i<lcp.size();i++){
        cout << lcp[i] << " ";
    }
    
    for (int i=2;i<lcp.size()-1;i++){
        if ((suf[i]>len1 && suf[i+1] < len1) || (suf[i]<len1 && len1<suf[i+1])){
            // if (lcp[i]!=0){
                s.push_back(max(suf[i],suf[i+1])-len1-1);
                e.push_back(max(suf[i],suf[i+1])-len1-1+lcp[i]);
                l.push_back(lcp[i]-1);
            // }
        }
    }
    for (int i=0;i<s.size();i++){
        cout << "(" << s[i] << " " << e[i] << " " << l[i] << ") ";
    }
    vector<int> v(s2.length()+1,0);
    cout<<s2.length()-dp(s,e,l);
    return 0;
}