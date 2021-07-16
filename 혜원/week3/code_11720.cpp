#include<iostream>
using namespace std;

int main(void) {
	int n;
	cin >> n;
	char ch;
	int sum = 0;
	for (int i = 0; i < n; i++) {
		cin >> ch;
		sum += (ch - '0');
	}

	cout << sum;
	return 0;
}