#include <bits/stdc++.h>

using namespace std;

typedef long long ll;

ll power(ll a, ll b, ll m) {
    ll ans = 1;
    while (b) {
        if (b % 2)
            ans = ans * a % m;
        a = a * a % m;
        b /= 2;
    }
    return ans;
}

ll rpower(ll a, ll b, ll m) {
    if (b == 0)
        return 1;
    ll ans = rpower(a, b / 2, m);
    ans = ans * ans % m;
    if (b % 2)
        ans = ans * a % m;
    return ans;
}
