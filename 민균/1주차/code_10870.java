package baekjoon.study.week1;


import java.util.Scanner;

public class n10870 {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int N = sc.nextInt();

        System.out.println(fibo(N));
    }
    static int fibo(int N){
        if (N == 0) return 0;
        if (N == 1) return 1;
        return fibo(N - 1) + fibo(N - 2);
    }
}
