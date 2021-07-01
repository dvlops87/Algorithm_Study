#include<stdio.h>
int main(){
	int tall[9];
	int total = 0;
	for(int i=0;i<9;i++){
		scanf("%d",&tall[i]);
		total+=tall[i];
	}
	for(int i=0;i<9;i++){
		int isDone = 0;
		for(int j=i+1;j<9;j++)
			if(total-tall[i]-tall[j]==100){
				tall[i]=tall[j]=0;
				isDone = 1;
			}
		if(isDone)break;
	}
	for(int i=0;i<9;i++)
		for(int j=0;j<9-1;j++)
			if(tall[j]>tall[j+1]){
				int tmp = tall[j];
				tall[j] = tall[j+1];
				tall[j+1]=tmp;
			}
	for(int i=2;i<9;i++)
		printf("%d\n",tall[i]);
	return 0;
}