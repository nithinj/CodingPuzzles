//
//  main.cpp
//  equal
//
//  Created by Nithin Johnson on 9/17/17.
//  Copyright © 2017 Nithin Johnson. All rights reserved.
//

#include <iostream>
#include <vector>
#include <limits.h>
#include <algorithm>

using namespace std;

int main() {
    int testcase = 0;
    int n = 0;
    vector<int> colleague;
    int i,j,k;
    int min_choco;
    vector<int> min_list(5);
    vector<int> colleague_dup;
    
    cin>> testcase;
    vector<int> min_attempts(testcase);
    
    for (i=0; i<testcase; i++) {
        min_attempts[i] = 0;
        cin >> n;
        if (colleague.size() <= n)
            colleague.resize(n);
        min_choco = INT_MAX;
        
        for (j=0; j<n; j++) {
            cin>>colleague[j];
            if (colleague[j] < min_choco)
                min_choco = colleague[j];
        }
        for (k=0; k < min_list.size(); k++) {
            colleague_dup = colleague;
            for (j=0; j<n; j++) {
                while (colleague_dup[j] > min_choco) {
                    if (colleague_dup[j]-5 >= min_choco)
                        colleague_dup[j] -= 5;
                    else if (colleague_dup[j]-2 >= min_choco)
                        colleague_dup[j] -= 2;
                    else
                        colleague_dup[j]--;
                    min_list[k]++;
                }
            }
            min_choco--;
        }
        
        min_attempts[i] = *min_element(min_list.begin(), min_list.end());
        colleague.clear();
        for (k=0; k < min_list.size(); k++)
            min_list[k] = 0;
    }
    
    for (i=0; i<testcase; i++) {
        cout << min_attempts[i]<<"\n";
    }
    
    return 0;
}
