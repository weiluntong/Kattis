#include <bits/stdc++.h>

using namespace std;

int main()
{
    string p, q;
    cin >> p >> q;
    if (p == "D")
    {
        for (int i = 0; i < q.length() - 1; i=i+2)
        {
            for (int j = 0; j < q[i+1] - '0'; j++)
            {
                cout << q[i];
            }
        }
        cout << endl;
    }
    else
    {
        for (int i = 0; i < q.length();)
        {
            int counter = 0;
            char c = q[i];
            while (q[i] == c && i < q.length())
            {
                counter++;
                i++;
            }
            cout << c << counter;
        }
        cout << endl;
    }
    return 0;
}
