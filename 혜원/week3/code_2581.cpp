#include <iostream>

int main() {
	int M = 0, N = 0, num = 0;
	int cnt = 0, res = 0, min = 0;
	std::cin >> M;
	std::cin >> N;
	for (int i = M; i < N + 1; i++) {
		for (int j = 1; j <= i; j++) {
			if (i%j == 0) cnt++;
		}
		if (cnt == 2) {
			num++;
			res += i;
			if (num == 1) min = i;
		}
		cnt = 0;
	}
	if (num == 0) {
		min = -1;
		std::cout << min << std::endl;
	} 
	else std::cout << res << std::endl << min << std::endl;

	return 0;
}