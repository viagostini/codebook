#include <bits/stdc++.h>

using namespace std;

int main () {
    int t, n0, n1, n2;

    cin >> t;
    while (t--) {
        cin >> n0 >> n1 >> n2;
        string s = "";
        
        if (n1 == 0)  {
            if (n0 == 0)
                for (int i= 0; i < n2+1; i++)
                    s += '1';
            else
                for (int i = 0; i < n0+1; i++)
                    s += '0';
        } else {
            for (int i = 0; i < n1 + 1; i++)
                if (i % 2)
                    s += '0';
                else
                    s += '1';
            s.insert(1, string(n0, '0'));
            s.insert(0, string(n2, '1'));
        }
        cout << s << endl;
    }
}
