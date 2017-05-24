//
//  main.cpp
//  extra_long_factorials
//
//  Created by Nithin Johnson on 6/26/17.
//  Copyright © 2017 Nithin Johnson. All rights reserved.
//

#include <iostream>

using namespace std;

int main() {
    
    int num;
    int a[200];
    int carry = 0;
    int m = 1;
    int i,j;
    int temp;
    
    cin>>num;
    
    for (i=0; i<200; i++)
        a[i] = 0;
    a[0] = 1;
    
    for (i=1; i<=num; i++) {
        for (j=0; j<m; j++) {
            temp = a[j]*i + carry;
            a[j] = temp%10;
            carry = temp/10;
        }
        while (carry) {
            a[m++] = carry%10;
            carry /= 10;
        }
    }
    
    for (i=m-1; i>=0; i--)
        cout<<a[i];
    
    return 0;
}
