#include <bits/stdc++.h>

using namespace std;

struct entry{
    int start;
    int end;
    int pill;
    double cost;
};

double calc(int duration, double ratio, int cost)
{
    return duration*ratio+cost;
}

int main()
{
    int n, p, c;
    cin>>n>>p>>c;
    int t;
    double x, y;
    map<int, double> mp;
    for(int i =0; i < p; i ++)
    {
        cin >> t >> x >> y;
        mp[t] = x/y;
    }
    
    vector<entry> s;
    s.push_back({n,n,-1,-1});
    
    for (auto it = mp.rbegin(); it != mp.rend(); it++)
    {
        pair<int, double> p = *it;
        entry old = s.back;
        if(old.cost > calc(p.first-, p.second, c))
        {
            
        }
    }
    
    return 0;
}
