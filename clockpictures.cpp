#include <bits/stdc++.h>

using namespace std;

int fail[1000005];

// Checks if two arrays are rotationally equvalent
bool KMPints(vector<long long> a, vector<long long> b){
    for(int i = 0; i < a.size(); i++) {
        b.push_back(b[i]);
    }
    int p = 0;
    for(int i = 1; i < a.size(); i++) {
        while(p && a[i] != a[p]) p = fail[p];
        if(a[i] == a[p]) p++;
        fail[i + 1] = p;
    }
    p = 0;
    for(auto &i : b) {
        while(p && i != a[p]) p = fail[p];
        if(i == a[p]) p++;
        if(p == a.size()) return true;
    }
    return false;
}

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);

    int n;
    cin >> n;
    vector<long long> clock1, clock2;
    for (int i = 0; i < n; i++)
    {
        long long j;
        cin >> j;
        clock1.push_back(j);
    }
    for (int i = 0; i < n; i++)
    {
        long long j;
        cin >> j;
        clock2.push_back(j);
    }

    sort(clock1.begin(), clock1.end());
    sort(clock2.begin(), clock2.end());

    vector<long long>delta1, delta2;
    for (int i = 1; i < clock1.size(); i++)
    {
        delta1.push_back(clock1[i]-clock1[i-1]);
    }
    delta1.push_back(360000-clock1.back()+clock1[0]);
    for (int i = 1; i < clock2.size(); i++)
    {
        delta2.push_back(clock2[i]-clock2[i-1]);
    }
    delta2.push_back(360000-clock2.back()+clock2[0]);

    cout << (KMPints(delta1, delta2) ? "possible" : "impossible") << endl;

    return 0;
}