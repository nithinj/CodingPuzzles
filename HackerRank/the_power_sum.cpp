//
//  the_power_sum.cpp
//  the_power_sum
//
//  Created by Nithin Johnson on 9/24/17.
//  Copyright © 2017 Nithin Johnson. All rights reserved.
//

#include <iostream>
#include <math.h>
#include <vector>

using namespace std;

int total=0;
int n;

void calculate(int needed, int next, int present_sum, vector<int> vec) {
    if(next == 0)
        return;
    if (present_sum > needed)
        return;
    if (needed == present_sum + pow(next, n))
        total++;
    if (needed > present_sum + pow(next, n)) {
        calculate(needed, next-1, present_sum, vec);
        calculate(needed, next-1, present_sum + pow(next, n), vec);
    }
    else
        calculate(needed, next-1, present_sum, vec);
}

int main() {
    int x;
    int start_at = 0;
    vector<int> a(0);
    
    cin>>x>>n;
    
    start_at = pow(x, 1.0/n);
    calculate(x, start_at--, 0, a);
    
    cout<<total;
    
    return 0;
}
