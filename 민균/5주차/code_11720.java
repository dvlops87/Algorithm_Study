package baekjoon.study.week5;

import java.util.Scanner;

public class code_11720 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        String s = sc.next();
        int sum = 0;
        for (int i = 0; i<N; i++){
            sum += Integer.parseInt(s[i]);
        }
        // ...........ㅜ
    }
}
