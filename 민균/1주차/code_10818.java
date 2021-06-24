package baekjoon.study.week1;

import java.util.Scanner;

public class n10818 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        int Arr[] = new int[N];

        for (int i = 0; i<Arr.length; i++){
            Arr[i] = sc.nextInt();
        }
        int min = Arr[0];
        int max = Arr[0];

        for (int i = 0; i<Arr.length; i++){
            if(Arr[i]<min){
                min = Arr[i];
            }
            else if(Arr[i]>max){
                max = Arr[i];
            }
        }
        System.out.printf("%d %d",min, max);
        sc.close();
    }
}
