// Bryon, Brian, Dustin, Garfield RM 305
#include <bits/stdc++.h>

using namespace std;

int main() {
	ifstream inFile;
	inFile.open("a.in");
	ofstream outFile;
	outFile.open("a.out");

	string input;
	unsigned int i;
	
	inFile >> i;
	inFile.ignore();

	for (int j = 0; j < i; j++)
	{
		int seen = -1;
		int numberOf = 0;
		getline(inFile, input);
		for (int k = 0; k < input.size(); k++)
		{
			if (seen != input.at(k) - '0')
			{
			    if (seen != -1)
			        outFile << numberOf << seen;
			    seen = input.at(k) - '0';
			    numberOf = 1;
			}
			else
			    numberOf++;
		}
		outFile << numberOf << seen;
		outFile << endl;
	}	

	return 0;
}

