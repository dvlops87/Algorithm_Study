package baekjoon.study.week6;

import java.util.Scanner;

public class code_11721 {
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        String input = sc.next();

        for(int i = 0; i<input.length(); i++){
            char a = input.charAt(i);
            System.out.print(a);
        if(i%10 == 9){ System.out.println(); }
        }
    }
}
