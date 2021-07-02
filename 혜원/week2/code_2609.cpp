//2609

#include <iostream>
using namespace std;

int gcd(int a, int b) {
	while (b != 0) {
		int r = a % b;
		a = b;
		b = r;
	}
	return a;
}
int lcm(int a, int b) {
	return a * b / gcd(a, b);
}

int main() {
	int a = 0, b = 0, min = 0, max = 0;

	cin >> a >> b;
	if (a > 10000 || b > 10000) return 0;

	max = gcd(a, b);
	min = lcm(a, b);

	cout << max << '\n' << min << endl;

	return 0;
}

////유클리드 호제법