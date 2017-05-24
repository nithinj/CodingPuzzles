//
//  main.cpp
//  decibinary_numbers
//
//  Created by Nithin Johnson on 3/5/18.
//  Copyright © 2018 Nithin Johnson. All rights reserved.
//
/* Steps:
 1. get rid of the sorting logic by computing for 10^16
 */

#include <iostream>
#include <math.h>
#include <list>
#include <vector>
#include <algorithm>
#include <map>
#include <time.h>

#define DEBUG 0
#define llong long long

using namespace std;

vector <map <int, vector<llong> > > big_array;
vector<llong> whole_rank_list;

int memorized(llong rem, int start, int pos, map <int, vector<llong> > * mem_list, llong num) {
    if (pos < 0)
        return 0;
    int found = 0;
    int i,k;
    llong val = 0;
    if (big_array.size() > rem) {
        map <int, vector<llong> > *rank_list = &big_array[rem];
        for (k=pos+1; k>0; k--) {
            if (rank_list->find(k) != rank_list->end()) {
                vector<llong> *rank_vec = &rank_list->at(k);
                for (i=0; i<rank_vec->size(); i++) {
                    val = num+(*rank_vec)[i];
                    if(DEBUG)
                        cout<<"\nUpdating memorized val:"<<val;
                    (*mem_list)[0].push_back(val);
                    (*mem_list)[start+1].push_back(val);
                }
                found = 1;
            }
        }
    }
    return found;
}

void reccuring_compute(vector<int> *vec, llong rem, int start, int pos, map <int, vector<llong> > * rank_list, llong num) {
    
    if (rem == 0) {
        if(DEBUG)
            cout<<"\nAdding to list:"<<num;
        (*rank_list)[0].push_back(num);
        (*rank_list)[start+1].push_back(num);
        return;
    }
    
    if (rem < 0 || pos < 0) {
        return;
    }
    
    if (memorized(rem, start, pos, rank_list, num))
        return;
    
    int multiplier = 1<<pos;
    if (rem > multiplier*9*2)
        return;
    int counter = (rem/multiplier > 9 ? 9 : (int)rem/multiplier);
    for (;counter>=0; counter--) {
        if ((start-pos) < vec->size())
            (*vec)[start-pos] = counter;
        else
            vec->push_back(counter);
        reccuring_compute(vec, rem-(counter*multiplier), (num||counter)?start:start-1, pos-1, rank_list, num + counter*pow(10, pos));
    }
}

void compute_rank_list(llong dec, llong x) {
    vector<int> vec;
    map <int, vector<llong> > rank_list;
    while (big_array.empty() || whole_rank_list.size() < x) {
        if (DEBUG)
            cout<<"\ncomputing...."<<dec;
        if (dec == 0) {
            rank_list[0].push_back(0);
            rank_list[1].push_back(0);
            dec++;
        } else {
            reccuring_compute(&vec, dec, ceil(log2(dec)), ceil(log2(dec)), &rank_list, 0);
            dec++;
        }
        big_array.push_back(rank_list);
        whole_rank_list.insert(whole_rank_list.begin(), rank_list[0].begin(), rank_list[0].end());
        vec.clear();
        rank_list.clear();
    }
}

int main() {
    //clock_t tStart = clock();
    ios::sync_with_stdio(false);
    int q;
    vector <llong> inp;
    vector <llong> copy;
    cin >> q;
    for(int a0 = 0; a0 < q; a0++) {
        llong x;
        cin >> x;
        inp.push_back(x);
        copy.push_back(x);
    }
    sort(copy.begin(), copy.end());
    compute_rank_list(0, copy[q-1]);
    for(int a0 = 0; a0 < q; a0++) {
         if (DEBUG)
             cout<<"\nResult:";
        cout << whole_rank_list[whole_rank_list.size()-inp[a0]] << endl;
    }
    return 0;
}


