//
//  main.cpp
//  counter_game
//
//  Created by Nithin Johnson on 9/19/17.
//  Copyright © 2017 Nithin Johnson. All rights reserved.
//

#include <iostream>
#include <vector>

#define ullong unsigned long long

using namespace std;

int main() {
    int T;
    int i;
    int count;
    ullong mask = 0;
    ullong input;
    
    cin >>T;
    vector<int> N(T, 0);
    
    for (i=0; i<T; i++) {
        cin >> input;
        count = 0;
        mask = ~(~0ull >> 1);
        
        while (input != 1) {
            while (!(input & mask))
                mask = mask >> 1;
            if ((input & (input-1)) == 0)
                mask = mask >> 1;
            input -= mask;
            count++;
        }
        N[i] = count;
    }
    
    for (i=0; i<T; i++) {
        if (N[i] % 2 == 0)
            cout << "Richard";
        else
            cout << "Louise";
        cout << "\n";
    }
    
    return 0;
}
