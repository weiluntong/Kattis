#include <bits/stdc++.h>

using namespace std;

int main()
{
    int p, q, s;
    cin >> p >> q >> s;
    for (int i = p; i <= s; i+=p)
    {
        if (i % q == 0)
        {
            cout << "yes\n";
            return 0;
        }
    }
    cout << "no\n";
    return 0;
}
