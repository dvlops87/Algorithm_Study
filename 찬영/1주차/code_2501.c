#include<stdio.h>
int main() {
	int p, q, result = 0, cnt = 0;
	scanf("%d%d", &p, &q);
	for (int i = 1; i <= p; i++) {
		if (!(p % i))cnt++;
		if (cnt == q) {
			result = i;
			break;
		}
	}
	printf("%d", result);
}