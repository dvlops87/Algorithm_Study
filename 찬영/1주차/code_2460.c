#include<stdio.h>
int main() {
	int minus, plus, max = 0, n = 0;
	for (int i = 0; i < 10; i++) {
		scanf("%d %d", &minus, &plus);
		n -= minus;
		n += plus;
		max = max < n ? n : max;
	}
	printf("%d\n", max);
	return 0;
}