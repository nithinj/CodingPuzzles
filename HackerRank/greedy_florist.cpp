//
//  main.cpp
//  Greedy_Florist
//
//  Created by Nithin Johnson on 9/15/17.
//  Copyright © 2017 Nithin Johnson. All rights reserved.
//

#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;


int getMinimumCost(int n, int k, vector < int > c){
    int min_cost = 0;
    int i, j=-1;
    sort(c.begin(), c.end(), greater<int>());
    for (i=0; i<n; i++) {
        if (i%k==0) {
            j++;
        }
        min_cost += (j+1)*c[i];
    }
    return min_cost;
}

int main() {
    int n;
    int k;
    cin >> n >> k;
    vector<int> c(n);
    for(int c_i = 0; c_i < n; c_i++){
        cin >> c[c_i];
    }
    int minimumCost = getMinimumCost(n, k, c);
    cout << minimumCost << endl;
    return 0;
}

