#include <bits/stdc++.h>

using namespace std;

int main()
{
    int n;
    cin >> n;
    vector<int> blameeOf(n+1);
    for(int i = 1; i <= n; i++)
        cin >> blameeOf[i];

    for (int i = 1; i <= n; i++)
    {
        vector<int> visited(n+1, false);
        int culprit = i;
        while(!visited[culprit])
        {
            visited[culprit] = true;
            culprit = blameeOf[culprit];
        }
        cout << culprit << " ";
    }
    cout << endl;
    return 0;
}