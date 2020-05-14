#include <bits/stdc++.h>

using namespace std;

vector<int> ans;

int main() {
    int t, n;

    cin >> t;

    while (t--) {
        int num = 0;
        cin >> n;
        int base = 1;

        ans.clear();

        while(n) {
            if (n % 10 != 0) {
                num += 1;
                ans.push_back((n%10) * base);
            }
            base *= 10;
            n /= 10;
        }

        cout << num << endl;
        for (auto a: ans) cout << a << " ";
        cout << endl;
    }
}