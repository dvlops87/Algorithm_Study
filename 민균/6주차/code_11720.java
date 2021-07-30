package baekjoon.study.week6;

import java.util.Scanner;

public class code_11720 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int sum = 0;
        int N = sc.nextInt();
        String input = sc.next();

        for (int i = 0; i < N; i++) {
            char a = input.charAt(i);
            sum += a - '0';
        }

        System.out.println(sum);
    }
}
