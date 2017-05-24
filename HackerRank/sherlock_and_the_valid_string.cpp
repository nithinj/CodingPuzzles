//
//  main.cpp
//  sherlock and the valid string
//
//  Created by Nithin Johnson on 6/28/17.
//  Copyright © 2017 Nithin Johnson. All rights reserved.
//

#include <iostream>

using namespace std;

int main(int argc, const char * argv[]) {
    int arr[26];
    int i,j;
    char str[100000];
    char *ch;
    int prev = 0;
    int compromises = 0;
    int reps[26];
    int max = 0;
    
    cin>>str;
    
    for (i=0; i<26; i++) {
        arr[i] = 0;
        reps[i]++;
    }
    
    for (ch=str; *ch; ch++)
        arr[(int)(*ch-'a')]++;
    
    for (i=0; i<26; i++)
        if (arr[i])
            for ( j=0; j<26; j++)
                if (arr[i] == arr[j])
                    reps[i]++;
    
    for (i=0; i<26; i++)
        if (reps[i] > reps[max])
            max = i;

    prev = arr[max];
    
    for (i=0; i<26; i++) {
        if(arr[i] && arr[i] != prev) {
            if (arr[i] == prev+1 || arr[i] == prev-1 || arr[i]-1 == 0)
                compromises++;
            if (compromises > 1 || ((arr[i] > prev+1 || arr[i] < prev-1) && arr[i]-1)) {
                cout << "NO";
                return 0;
            }
        }
    }
    
    cout<< "YES";
    return 0;
}
