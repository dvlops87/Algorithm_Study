package baekjoon.study.week1;

import java.util.Scanner;

public class n2460 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int sum = 0, ans = 0;

        for (int i = 0; i<10; i++){
            int in,out;
            for(int j = 0; j<2; j++){
                in = sc.nextInt();
                out = sc.nextInt();
                sum += in - out;
            }
            if(ans < sum) {
                ans = sum;
            }
        }
        System.out.println(ans);
        sc.close();
    }
}
