#include <bits/stdc++.h>

using namespace std;

int main()
{
    int n;
    string directions;
    cin >> n >> directions;
    int counter = 1;
    for (int i = 0; i < directions.length(); i++)
    {
        if (directions[i] == 'L')
            counter++;
        else
        {
            int pos = i + 1;
            do
            {
                cout << pos << endl;
                pos--;
                counter--;
            } while (counter > 0);
            counter = 1;
        }
    }
    int pos = directions.length() + 1;
    do
    {
        cout << pos << endl;
        pos--;
        counter--;
    } while (counter > 0);
    return 0;
}
