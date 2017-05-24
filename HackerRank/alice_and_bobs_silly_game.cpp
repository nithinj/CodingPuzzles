//
//  alice_and_bobs_silly_game.cpp
//  Alice and Bob's Silly Game
//
//  Created by Nithin Johnson on 9/24/17.
//  Copyright © 2017 Nithin Johnson. All rights reserved.
//

#include <iostream>
#include <vector>
#include <math.h>

using namespace std;

int how_many_primes(int num) {
    //Sieve of Eratosthenes
    
    int count = 0;
    vector<int> arr(num-1, 0);
    
    if (num==1)
        return 0;
    
    for (int i=2; i<= num; i++)
        arr[i-2] = i;
    
    for(int i=0; arr[i]*arr[i] <= num;) {
        for (int j=i+arr[i]; j<num-1; j=j+arr[i])
            arr[j] = -1;
        while(arr[++i] == -1);
    }
    
    for(int i=0; i < num-1; i++)
        if (arr[i] != -1)
            count++;
    
    return count;
}

int main() {
    /* find the prime numbers between 2 and n
     if it is even Alice wins, else Bob*/
    int t;
    int i;
    int num;

    cin>>t;
    
    for (i=0; i<t; i++) {
        cin>> num;
        if (how_many_primes(num)%2 == 1)
            cout<<"Alice";
        else
            cout<<"Bob";
    cout<<"\n";
    }
    
    return 0;
}
