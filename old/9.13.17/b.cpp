//Brian, Dustin, Garfield RM 305
#include <bits/stdc++.h>

using namespace std;

string decrypt(const string& s, uint n)
{
	vector<string> in;
	for (int i = 0; i < s.size(); i += n)
		in.push_back(s.substr(i, n));
		
	for (int k = 0; k < in.size(); k++)
		if (k % 2)
		reverse(in[k].begin(), in[k].end());
	
	string out;
	for (int i = 0; i < n; i++)
		for (int j = 0; j < in.size(); j++)
			out += in[j][i];
		
	return out;
}

int main() {
	ifstream inFile("b.in");
	ofstream outFile("b.out");

	string input;
	unsigned int n;
	

	while (inFile >> n && n)
	{
		string s;
		inFile >> s;
		outFile << decrypt(s, n) << endl;
	} 
	
	return 0;
}

