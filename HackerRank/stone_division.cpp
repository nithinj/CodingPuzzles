//
//  stone_division.cpp
//  stone_division
//
//  Created by Nithin Johnson on 11/6/17.
//  Copyright © 2017 Nithin Johnson. All rights reserved.
//

#include <iostream>
#include <stack>
#include <algorithm>

using namespace std;

u_long m;
u_long *divisors;

int simulate(u_long n, int coin, int defensive) {
    int i;
    
    while(1) {
        if (n == 1)
            return (coin+1)%2;
        
        for (i=0; i<m; i++) {
            if ((n%divisors[i] == 0) && (divisors[i]%2 == 0)) {
                n/=divisors[i];
                return(coin);
            } else if ((n%divisors[i] == 0) && defensive) {
                if (coin == simulate(n/divisors[i], (coin+1)%2, defensive))
                    return coin;
            }
        }
        
        /* we cannot decide the winner here, also time to play defensive. choose a number so that the opponent cannot win the game in the up coming steps */
        if (i==m && !defensive)
            return simulate(n, coin, 1);
        else if (i==m)
            return ((coin+1)%2);
        
        coin=(coin+1)%2;
    }
}

int main() {
    u_long n;
    int i;
    stack <u_long> st;
    
    cin>>n>>m;
    divisors = new u_long[m];
    for (i=0; i<m; i++) {
        cin>>divisors[i];
    }
    
    //sorting in descending order to make the simulation faster :)
    sort(divisors, divisors+m, std::greater<u_long>());
    
    simulate(n, 0, 0) == 0 ? cout<<"First\n": cout<<"Second\n";
    
    return 0;
}
