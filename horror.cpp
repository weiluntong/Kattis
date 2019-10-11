#include <bits/stdc++.h>

using namespace std;

void bfs(int s, const vector<vector<int>> &neighborsOf, vector<int> &weights)
{
    vector<bool> visited(weights.size());
	queue<pair<int, int>> q;
    q.push({s, 0});
    visited[s] = true;
    while (!q.empty())
    {
        int node = q.front().first;
        int nodeWeight = q.front().second;
        // Do weights logic
        weights[node] = min(weights[node], nodeWeight);
        q.pop();
        for (auto neighbor : neighborsOf[node])
        {
            if (!visited[neighbor])
            {
                visited[neighbor] = true;
                q.push({neighbor, weights[node]+1});
            }
        }
    }
}

int main()
{
    int N, H, L;
    cin >> N >> H >> L;

    vector<int> movies(N, INT_MAX / 2);
    vector<int> x;
    vector<vector<int>> adj(N);

    while (H--)
    {
        int x_i;
        cin >> x_i;
        x.push_back(x_i);
    }

    while(L--)
    {
        int a, b;
        cin >> a >> b;
        adj[a].push_back(b);
        adj[b].push_back(a);
    }
    for (auto start : x)
    {
        bfs(start, adj, movies);
    }

    int answer = -1;
    for (int i = 0; i < N; i++)
    {
        if (movies[i] > movies[answer]) answer = i;
        if (movies[i] == INT_MAX / 2) break;
    }

    cout << answer << endl;
    return 0;
}