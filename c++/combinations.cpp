#include <bits/stdc++.h>

using namespace std;

vector<vector<int>> pascal(int MAXN) {
    vector<vector<int>> C(MAXN, vector<int>(MAXN, 0));
    C[0][0] = 1;
    for (int n = 1; n <= MAXN; ++n) {
        C[n][0] = C[n][n] = 1;
        for (int k = 1; k < n; ++k)
            C[n][k] = C[n - 1][k - 1] + C[n - 1][k];
    }
    return C;
}