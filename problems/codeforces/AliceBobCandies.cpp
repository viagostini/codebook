#include <bits/stdc++.h>

using namespace std;

int i, t, n, a, b, suma, preva, prevb, sumb, ja, jb;
vector<int> ai;

int main() {
    cin >> t;
    while(t--) {
        cin >> n;

        ai.clear();
        suma = sumb = 0;
        preva = prevb = 0;

        for (int i = 0; i < n; i++) {
            int x;
            cin >> x;
            ai.push_back(x);
        }

        ja = 0;
        jb = n-1;
        for (i = 0; ja <= jb; i++) {
            // alice = even rounds
            int cur = 0;
            if (i % 2 == 0) {
                // alice
                while (cur <= prevb && ja <= jb) {
                    cur += ai[ja];
                    suma += ai[ja++];
                }
                preva = cur;
            }
            else {
                while (cur <= preva && ja <= jb) {
                    cur += ai[jb];
                    sumb += ai[jb--];
                }
                prevb = cur;
            }
        }
        cout << i << " " << suma << " " << sumb << endl;

    }    
}