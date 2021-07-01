#include<stdio.h>
int getGCD(int x, int y){
	if(y==0)
		return x;
	else
		return getGCD(y,x%y);
}
int main(){
	int x, y, gcd, lcm;
	scanf("%d%d",&x,&y);
	gcd = getGCD(x>y?x:y, x>y?y:x);
	lcm = x*y/gcd;
	printf("%d\n%d",gcd,lcm);
	return 0;
}