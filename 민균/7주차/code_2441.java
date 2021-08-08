package baekjoon.study.week7;

import java.util.Scanner;

public class code_2441 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();

        for(int i=0; i<n; i++){
            for(int j=0; j<n; j++){
                System.out.print(" ");
            }
            for(int k=0; k<32; k++){
                System.out.print(" ");
            }
            System.out.println();
        }
    }
}
