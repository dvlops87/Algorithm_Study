#include<stdio.h>
int main() {
	int from, to, num = 1, cnt = 1, total = 0;
	scanf("%d%d", &from, &to);
	while (1) {
		for (int i = 0;i < num;i++) {
			if (cnt >= from && cnt <= to)
				total += num;
			if (cnt == to) {
				printf("%d\n", total);
				return 0;
			}
			cnt++;
		}
		num++;
	}
}