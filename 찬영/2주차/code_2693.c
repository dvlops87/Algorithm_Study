#include<stdio.h>
int main(){
	int t, a[10], index;
	scanf("%d",&t);
	for(int i=0;i<t;i++){
		for(int j=0;j<10;j++)
			scanf("%d",&a[j]);
		for(int j=0;j<10;j++)
			for(int k=0;k<9;k++)
				if(a[i]>a[k+1]){
					int tmp = a[k];
					a[k] = a[k+1];
					a[k+1]=tmp;
				}
		printf("%d\n",a[7]);
	}
	return 0;
}