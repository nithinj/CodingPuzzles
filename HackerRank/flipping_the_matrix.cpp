//
//  main.cpp
//  flipping_the_matrix
//
//  Created by Nithin Johnson on 9/17/17.
//  Copyright © 2017 Nithin Johnson. All rights reserved.
//

#include <iostream>
#include <vector>

using namespace std;

#define ulong unsigned long

int max_elem(int a, int b, int c, int d) {
    int max=0;
    if (max < a)
        max=a;
    if(max < b)
        max = b;
    if(max < c)
        max = c;
    if(max < d)
        max = d;
    return max;
}

int main() {
    int queries;
    int n;
    vector<vector<int> > matrix;
    int i, row, col;
    
    cin>>queries;
    vector<ulong> sum(queries, 0);
    
    for (i=0; i<queries; i++) {
        cin>>n;
        matrix.resize(2*n);
        for (row=0; row<2*n; row++) {
            matrix[row].push_back(0);
            matrix[row].resize(2*n, 0);
            for (col=0; col<2*n; col++)
                cin>> matrix[row][col];
        }
        
        for (row=0; row<n; row++)
            for (col=0; col<n; col++) {
                sum[i] += max_elem(matrix[row][col], matrix[2*n-1-row][col], matrix[row][2*n-1-col], matrix[2*n-1-row][2*n-1-col]);
            }
    }
    
    for (i=0; i<queries; i++)
        cout << sum[i] << "\n";
    
    return 0;
}
