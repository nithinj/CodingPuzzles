#include<iostream>

using namespace std;

int main() {
	int n, k, i, j = 0;
	cin >> n >> k;
	int *arr = new int[n];
	for (i = 0; i < n; i++)
		cin >> arr[i];
	for (i = k; j < n-1; i = (i + 1) % n) {
		cout << arr[i] << " ";
		j++;
	}
	cout << arr[i];
	delete[] arr;
	return 0;
}
