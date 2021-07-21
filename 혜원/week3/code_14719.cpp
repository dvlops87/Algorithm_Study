#include <iostream>
#include <algorithm>
using namespace std;
int arr[502];
int row, col;

int main() {
	ios_base::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);
	int result = 0, r, l;
	cin >> row >> col;
	for (int i = 1; i <= col; i++)
		cin >> arr[i];
	for (int i = 2; i < col; i++) {
		r = l = arr[i];
		for (int j = 1; j < i; j++)
			l = max(l, arr[j]);
		for (int j = i + 1; j <= col; j++)
			r = max(r, arr[j]);
		result += (min(r, l) - arr[i]);
	}
	cout << result;
	return 0;
}