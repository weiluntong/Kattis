#include <bits/stdc++.h>

using std::cin;
using std::cout;
using std::endl;
using std::stack;

int main() {
    int n;
    cin >> n;

    stack<int> remaining;

    while (n--) {
        int i;
        cin >> i;
        if (remaining.empty()) remaining.push(i);
        else if ((remaining.top() + i) % 2) remaining.pop();
        else remaining.push(i);
    }
    cout << remaining.size() << endl;
    return 0;
}