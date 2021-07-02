package baekjoon.study.week2;

import java.util.Arrays;
import java.util.Scanner;

public class code_2693 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int T = sc.nextInt();
        int[] arr = new int[10];
        for (int i = 0; i < T; i++) {
            for (int j = 0; j < arr.length; j++) {
                arr[j] = sc.nextInt();
            }
            Arrays.sort(arr);
            System.out.println(arr[7]);
        }
        sc.close();
    }
}
