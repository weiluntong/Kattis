#include <bits/stdc++.h>

using namespace std;

struct KMP_Match {
    vector<int> T;
    string pat;
    KMP_Match() {};
    KMP_Match(string pattern) : pat(pattern) {this->buildTable(pat);};
    void buildTable(string pattern) {
        pat = pattern;
        T.clear();
        T.resize(pat.length()+1);
        int i = 0, j = -1;
        T[i] = j;
        while(i < pat.size()) {
            while(j >= 0 && pat[i] != pat[j]) j = T[j];
            i++, j++;
            T[i] = j;
        }
    }
    string find(string txt) {
        int m = 0, i = 0;
        while(m + i < txt.length()) {
            if(pat[i] == txt[m+i]) {
                if(i == pat.length()-1) {
                    txt.erase(txt.begin()+m, txt.begin()+m+pat.size());
                    // m = m + i - T[i];
                    m = max(0, m-int(pat.size()));
                    i = -1;
                }
                i++;
            } else {
                if(T[i] != -1) {
                    m = m + i - T[i];
                    i = T[i];
                } else {
                    i = 0;
                    m++;
                }
            }
        }
        return txt;
    }
};

int main() {
    int n;
    string pat;

    while(cin >> n >> pat)
    {
        string line;
        cin.ignore();
        KMP_Match kmp(pat);
        while(n--)
        {
            getline(cin, line);
            cout << kmp.find(line) << endl;
        }

    }
    return 0;
}