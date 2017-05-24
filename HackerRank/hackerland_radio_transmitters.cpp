//
//  hackerland_radio_transmitters
//
//  Created by Nithin Johnson on 7/9/17.
//  Copyright © 2017 Nithin Johnson. All rights reserved.
//

#include <iostream>
#include <algorithm>

using namespace std;

int main() {
    uint n, k;
    uint *x=NULL;
    uint i;
    int transmitters = 1;
    int range = 0;
    int placed = 0;
    
    cin>>n>>k;
    x = (uint *)malloc(sizeof(int)*n);
    for (i=0; i<n; i++)
        cin >> x[i];
    
    if (n == 0) {
        cout<<"0";
        return transmitters;
    }
    
    sort(x, x+n);
    range = k + x[0];
    
    for (i=1; i<n; i++) {
        if (x[i] > range) {
            if (placed || (x[i] - x[i-1] > k)) {
                range = x[i] + k;
                placed = 0;
                transmitters++;
            } else {
                range = x[i-1] +k;
                placed = 1;
            }
        }
    }
    
    cout <<transmitters;
    return 0;
    
}
