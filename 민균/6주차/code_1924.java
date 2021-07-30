package baekjoon.study.week6;

import java.util.Scanner;

public class code_1924 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int month = sc.nextInt();
        int day = sc.nextInt();

        int[] mon = {31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31};
        String [] weak = {"SUN", "MON", "TUE", "WED", "THU", "FRI", "SAT"};
        int sum = day;
        for(int i = 0; i<month-1; i++){
            sum += mon[i];
        }
        System.out.println(weak[sum%7]);

    }
}
