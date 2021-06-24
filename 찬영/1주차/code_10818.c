#include<stdio.h>
#include <limits.h>
int main() {
	int n, tmp, big = INT_MIN, small = INT_MAX;
	scanf("%d", &n);
	for (int i = 0; i < n; i++) {
		scanf("%d", &tmp);
		big = big < tmp ? tmp : big;
		small = small > tmp ? tmp : small;
	}
	printf("%d %d\n", small, big);
	return 0;
}