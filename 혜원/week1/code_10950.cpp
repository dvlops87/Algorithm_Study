#include <iostream>

int main() {
	int num = 0, a = 0, b = 0;

	std::cin >> num;
	for (int i = 1; i <= num; i++) {
		std::cin >> a >> b;
		if (a <= 0) return 0;
		if (b >= 10) return 0;

		std::cout << a + b << std::endl;
	}
	
	return 0;
}

//처음에 endl을 써주지 않아서 틀렸음
//endl 앞에 std를 붙여야 하는지 몰랐음