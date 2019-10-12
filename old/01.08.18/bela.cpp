#include <bits/stdc++.h>

using namespace std;

int** returnTable();
char cvtIdx(char);

int main()
{
    int n = 0;
    int points = 0;
    char b;
    int** table = returnTable();

    cin >> n >> b;
    for (int i = 0; i < n * 4; i++)
    {
        string input;
        cin >> input;
        input[0] = cvtIdx(input[0]);
        input[1] = (input[1] == b) ? 1 : 0;
        points += table[input[0]][input[1]];
    }
    cout << points << endl;
    return 0;
}

int** returnTable()
{
    int** table = new int*[7];
    for (int i = 0; i < 7; i++)
    {
        table[i] = new int[2];
    }

    table[0][0] = 11;
    table[0][1] = 11;

    table[1][0] = 4;
    table[1][1] = 4;

    table[2][0] = 3;
    table[2][1] = 3;

    table[3][0] = 2;
    table[3][1] = 20;

    table[4][0] = 10;
    table[4][1] = 10;

    table[5][0] = 0;
    table[5][1] = 14;

    table[6][0] = 0;
    table[6][1] = 0;

    return table;
}

char cvtIdx(char Char)
{
    if (Char == 65)
        return 0;
    if (Char == 75)
        return 1;
    if (Char == 81)
        return 2;
    if (Char == 74)
        return 3;
    if (Char == 84)
        return 4;
    if (Char == 57)
        return 5;
    return 6;
}