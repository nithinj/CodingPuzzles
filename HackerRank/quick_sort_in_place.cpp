//
//  main.cpp
//  quick_sort_in_place
//
//  Created by Nithin Johnson on 7/9/17.
//  Copyright © 2017 Nithin Johnson. All rights reserved.
//

#include <iostream>

using namespace std;

static int n;

void print_output(int *arr) {
    int i;
    for (i=0; i<n; i++)
        cout << arr[i] << " ";
    cout << "\n";
}

int partition(int *arr, int low, int high) {
    int pivot = arr[high];
    int i = low;
    int j;
    for (j=low; j<high; j++)
        if (arr[j] < pivot) {
            swap(arr[i++], arr[j]);
        }
    swap(arr[i], arr[high]);
    return i;
}

void quick_sort(int *arr, int low, int high) {
    int p;
    if (low < high) {
        p = partition(arr, low, high);
        print_output(arr);
        quick_sort(arr, low, p-1);
        quick_sort(arr, p+1, high);
    }
}

int main() {
    int *arr = NULL;
    int i;
    
    cin >> n;
    arr = (int *)malloc(sizeof(int)*n);
    for (i=0; i<n; i++)
        cin >> arr[i];
    
    quick_sort(arr, 0, n-1);
    
    return 0;
}
