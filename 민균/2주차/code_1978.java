package baekjoon.study.week2;

import java.util.Scanner;

public class code_1978 {

    public static boolean isPrime(int num){
        if (num == 1) return false;
        for (int i = 2; i <num; i++){
            if (num%i==0) return false;
        }
        return true;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        int []arr = new int[N];
        int cnt = 0;
        for (int i = 0; i<N; i++){
            arr[i] = sc.nextInt();
            if(isPrime(arr[i])) cnt++;
        }
        System.out.println(cnt);
        sc.close();
    }
}
