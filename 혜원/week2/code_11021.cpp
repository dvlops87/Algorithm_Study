#include <iostream>

int main() {

	int a = 0, b = 0, T = 0, x = 1;

	std::cin >> T;
	
	while (T--) {

		std::cin >> a >> b;
		std::cout << "Case #" << x << ": " << a + b << std::endl;
		x++;
	}
	return 0;
}