#include <bits/stdc++.h>

using namespace std;

int main ()
{
    int x = 1;
    int y = 250;
    int c = 25;
    for (int i = 0; i < c; i++)
    {
        x = x*10;
        cout << x / y;
        x = x%y;
    }
    cout << endl;
}
