#include <cstdio>
#include <cstring>
#include <iostream>
using namespace std;

int main() {
    int i = 2;
    while (1) {
        printf("? %d %d\n", 1, i);
        fflush(stdout);
        long long r1, r2;
        cin >> r1;
        if (r1==0){
            return 0;
        }
        if (r1 == -1){
            cout << "! " << i-1 << "\n";
            fflush(stdout);
            return 0;
        }
        printf("? %d %d\n", i, 1);
        fflush(stdout);
        cin >> r2;
        if (r2==0){
            return 0;
        }
        if (r1 != r2){
            printf("! %d\n", r1 + r2);
            fflush(stdout);
            return 0;
        }
        i++;
    }
}