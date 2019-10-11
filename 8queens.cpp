#include <bits/stdc++.h>

using namespace std;

bool isSafe(bool board[8][8], int row, int col) 
{ 
    int i, j; 
  
    for (i = 0; i < 8; i++) 
    {
        if (board[row][i] && i != col) 
            return false; 
        if (board[i][col] && i != row)
            return false;
    }
  
    for (i = row-1, j = col-1; i >= 0 && j >= 0; i--, j--) 
    {
        if (board[i][j]) 
        {
            return false; 
        }
    }
  
    for (i = row+1, j = col+1; j < 8 && i < 8; i++, j++) 
    {
        if (board[i][j]) 
        {
            return false; 
        }
    }
    
    for (i = row-1, j = col+1; i >= 0 && j < 8; i--, j++)
    {
        if (board[i][j])
        {
            return false;
        }
    }
    
    for (i = row+1, j = col-1; i < 8 && j >= 0; i++, j--)
        if (board[i][j])
            return false;
  
    return true; 
} 

int main() {
    bool board[8][8] = { { 0, 0, 0, 0, 0, 0, 0, 0 }, 
                        { 0, 0, 0, 0, 0, 0, 0, 0 }, 
                        { 0, 0, 0, 0, 0, 0, 0, 0 }, 
                        { 0, 0, 0, 0, 0, 0, 0, 0 }, 
                        { 0, 0, 0, 0, 0, 0, 0, 0 }, 
                        { 0, 0, 0, 0, 0, 0, 0, 0 }, 
                        { 0, 0, 0, 0, 0, 0, 0, 0 }, 
                        { 0, 0, 0, 0, 0, 0, 0, 0 } }; 
    int queensNum = 0;
    for (int i = 0; i < 8; i++)
    {
        string row;
        cin >> row;
        for (int j = 0; j < 8; j++)
        {
            if(row[j] == '*')
            {
                board[i][j] = true;
                queensNum++;
            }
        }
    }
    if (queensNum != 8)
    {
        cout << "invalid" << endl;
        return 0;
    }
    for (int i = 0; i < 8; i++)
    {
        for (int j = 0; j < 8; j++)
        {
            if (board[i][j]) {
                if (!isSafe(board, i, j)) {
                    cout << "invalid" << endl;
                    return 0;
                }
            }
        }
    }
    cout << "valid" << endl;
    return 0;
}