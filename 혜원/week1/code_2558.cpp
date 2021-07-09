#include <iostream>

int main() {
	int a = 0, b = 0, total = 0;

	std::cin >> a;
	std::cin >> b;
	if (a <= 0) return 0;
	if (b >= 10) return 0;

	total = a + b;

	std::cout << total;
	return 0;

}