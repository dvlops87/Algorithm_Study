package baekjoon;

import java.util.Scanner;

public class n10952 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int num1 =0, num2 = 0;

        while(num1 == 0 && num2 == 0){
            num1 = sc.nextInt();
            num2 = sc.nextInt();

        }
        System.out.println(num1+num2);
    }
}
