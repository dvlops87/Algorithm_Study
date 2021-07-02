package baekjoon.study.week2;

import java.util.Scanner;

public class code_11022 {

    public static void printCase(int i, int a, int b){
        System.out.printf("Case #%d: ",i+1);
        System.out.printf("%d + %d = %d", a, b, a+b);
    }
    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        int T = sc.nextInt();
        for (int i = 0; i<T; i++){
            int a = sc.nextInt();
            int b = sc.nextInt();
            printCase(i, a, b);
        }
        sc.close();
    }
}
