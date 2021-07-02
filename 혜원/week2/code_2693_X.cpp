//2693 ??

#include <iostream>

using namespace std;

int main() {
	int N = 3, T = 0, num = 0;
	int arr[10] = { 0 };
	cin >> T;
	while (T--) {
		for (int i = 0; i < N; i++) {
			cin >> arr[i];
		}
		for (int i = 0; i < N - 1; i++) {
			for (int j = i + 1; j < N; j++) {
				if (arr[i] > arr[j]) {
					num = arr[j];
					arr[j] = arr[i];
					arr[i] = num;
				}
			}
		}
		cout << arr[7] << endl;
		//arr[10] = { 0 };

	}
	return 0;
}