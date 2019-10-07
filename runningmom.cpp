#include <bits/stdc++.h>

using namespace std;

#define umap unordered_map

bool detectCycle(const string &node, umap<string, vector<string>> &neighborsOf, umap<string, int> inDegrees)
{
	queue<string> q;
	q.push(node);
	while (!q.empty())
	{
		string city = q.front();
		q.pop();
		if (inDegrees[city] == -1)
			return true;
		for (auto neighbor : neighborsOf[city])
		{
			inDegrees[neighbor] -= 1;
			q.push(neighbor);
		}
	}
	return false;
}

int main()
{
	int n;
	cin >> n;

	umap<string, vector<string>> adj;
	umap<string, int> inDegrees;
	for (int i = 0; i < n; i++)
	{
		string o, d;
		cin >> o >> d;
		adj[o].push_back(d);
		inDegrees[d] += 1;
	}
	string s;
	while (cin >> s)
	{
		bool safe = detectCycle(s, adj, inDegrees);
		cout << s << " " << (safe ? "safe" : "trapped") << endl;
	}
}