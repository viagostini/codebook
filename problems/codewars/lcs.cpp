#include <vector>
#include <iostream>
#include <string>
#include <algorithm>

using namespace std;

// https://www.codewars.com/kata/593ff8b39e1cc4bae9000070


int dp[100][100];

void compute_lcs_table(const string& x, const string& y) {
    int xn = x.length();
    int yn = y.length();

    /* 
       dp[i][j] = length of lcs(x[0..i-1], y[0..j-1]) or alternatively
                  length of lcs considering first i letters in x and first j letters in y
       
       if last characters match, we take from both strings and add 1
       if not, we take the one that yields bigger lcs
    */
    
    for (int i = 1; i <= xn; i++) {
        for (int j = 1; j <= yn; j++) {
            if (x[i-1] == y[j-1])
                dp[i][j] = dp[i-1][j-1] + 1;
            else
                dp[i][j] = max(dp[i][j-1], dp[i-1][j]);
        }
    }
}

string reconstruct_lcs(const string& x, const string& y, int i, int j) {
    // either subarray is empty
    if (i == 0 || j == 0)
        return "";

    // if last character match, we move up diagonally
    if (x[i-1] == y[j-1])
        return reconstruct_lcs(x, y, i-1, j-1) + x[i-1];

    // otherwise, we move in direction of greatest lcs length
    if (dp[i][j-1] > dp[i-1][j])
        return reconstruct_lcs(x, y, i, j-1);
    else
        return reconstruct_lcs(x, y, i-1, j);
}

string lcs(const string& x, const string& y) {
    compute_lcs_table(x, y);
    return reconstruct_lcs(x, y, int(x.length()), int(y.length()));
}