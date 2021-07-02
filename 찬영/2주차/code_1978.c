#include<stdio.h>
int main() {
	int n, tmp, cnt = 0, isDec = 0;
	scanf("%d", &n);
	for (int i = 0;i < n;i++) {
		isDec = 1;
		scanf("%d", &tmp);
		if (tmp == 1 || tmp == 0)continue;
		for (int j = 2;j < tmp;j++)
			if (tmp % j == 0)isDec = 0;
		if (isDec)cnt++;
	}
	printf("%d\n", cnt);
	return 0;
}