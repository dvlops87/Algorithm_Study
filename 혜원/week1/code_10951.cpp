#include <iostream>

int main() {
	int a = 0, b = 0;

	while (std::cin >> a >> b) {
		if (a <= 0) return 0;
		if (b >= 10) return 0;
		std::cout << a + b << std::endl;
	}
	
	return 0;
}

//while문 사용