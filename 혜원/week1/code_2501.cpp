#include <iostream>

int main() {
	int N = 0, K = 0, i = 1, j = 0, x = 0;
	int ind[100] = { 0 };

	std::cin >> N >> K;
	if (N < 0 || N > 10000 + 1) return 0;
	if (K < 0 || K > N + 1) return 0;

	for (i; i < N + 1; i++) {
		x = N % i;
		if (x == 0) {
			ind[j] = i;
			j++;
		} 
	}
	std::cout << ind[K - 1];

	return 0;
}

//런타임 에러(OutOfBounds) : 컨테이너 또는 배열에서 할당된 경계를 넘어가는 접근 발생
