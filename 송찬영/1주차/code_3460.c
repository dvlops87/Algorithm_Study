#include<stdio.h>
int main() {
	int t, n, cnt;
	scanf("%d", &t);
	for (int i = 0; i < t; i++) {
		scanf("%d", &n);
		int tmp;
		for (cnt = 0, tmp = 1; tmp <= n; cnt++, tmp *= 2);
		for (int j = 0; j < cnt; j++)
			if (n & (1 << j))
				printf("%d ", j);
		printf("\n");
	}
}