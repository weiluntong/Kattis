#include <bits/stdc++.h>

using namespace std;

int main()
{
  int n;
  cin >> n;

  while(n--)
  {
    vector<string> numbers;
    int m;
    cin >> m;
    while (m--)
    {
      string number;
      cin >> number;
      numbers.push_back(number);
    }
    sort(numbers.begin(), numbers.end()); // lexiographical sort
    bool concurrent = true;
    for (int i = 0; i < numbers.size() - 1; i++)
    {
        if (numbers[i+1].size() >= numbers[i].size())
        {
          if (numbers[i+1].find(numbers[i]) == 0)
          {
            concurrent = false;
            break;
          }
        }
    }

      if (concurrent)
        cout << "YES" << endl;
      else
        cout << "NO" << endl;
  }

  return 0;
}
