//2309 ??

#include <iostream>

int main() {
	int arr[8] = { 0 };
	int num = 0;
	int b = 0;

	for (int i = 0; i < 8; i++) {
		std::cin >> arr[i];
		for (int j = i + 1; j < 9; j++) {
			if (arr[i] > arr[j]) {
				num = arr[i];
				arr[i] = arr[j];
				arr[j] = num;
			}
		}
	}


	for (int i = 0; i < 9; i++) {
		std::cout << arr[i] << std::endl;
	}
	return 0;
