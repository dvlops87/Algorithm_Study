package baekjoon.study.week1;

import java.util.Scanner;

public class code_2460 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int [][] people = new int [10][2];
        for (int i = 0; i<10; i++){
            people[i][0] = sc.nextInt();
            people[i][1] = sc.nextInt();
        }

        int sum = 0;
        int max = 0;

        for (int i = 0; i<10; i++) {
            sum += people[i][1] - people[i][0];
            max = Integer.max(max, sum); //큰 값 리턴
        }
        System.out.println(max);
        sc.close();
    }
}
