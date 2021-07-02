#include <iostream>
using namespace std;

int main() {
	int N = 0, cnt = 0, res = 0;
	int arr[1001] = { 0 };

	cin >> N;
	if (N > 100) return 0;

	for (int i = 0; i < N; i++) {
		cin >> arr[i];
		for (int j = 1; j <= arr[i]; j++) {
			if (arr[i] % j == 0) cnt++;
		}
		if (cnt == 2) res++;
		cnt = 0;
	}
	cout << res;

	return 0;
}

////소수를 구하는 방법 다시 보자.