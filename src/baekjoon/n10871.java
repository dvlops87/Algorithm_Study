package baekjoon;

import java.util.Scanner;

public class n10871 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = 0, X = 0;
        N = sc.nextInt();
        X = sc.nextInt();
        int[] num = new int[N];
        for (int i = 0; i < N; i++) {

            num[i] = sc.nextInt();
            if (num[i] < X) {
                System.out.printf("%d ", num[i]);
            }
        }

    }
}
