package baekjoon.study.week5;

import java.util.Scanner;

public class code_10953 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int T = 0;
        int arr[] = new int[2];
        String line = new String();
        T = sc.nextInt();
        for(int i = 0; i<T; i++){
            line = sc.next();
            String s[] = line.split(",");
            System.out.println(Integer.parseInt(s[0]) + Integer.parseInt(s[1]));
        }
    }
}
