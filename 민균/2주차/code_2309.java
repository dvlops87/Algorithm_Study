package baekjoon.study.week2;

import java.util.Arrays;
import java.util.Scanner;

public class code_2309 {
    public static void main(String[] args) {
        int num[] = new int[9];
        int sum = 0;
        Scanner sc = new Scanner(System.in);
        for (int i = 0; i<num.length; i++){
           num[i] = sc.nextInt();
           sum += num[i];
        }
        Arrays.sort(num);

        for (int i = 0; i<num.length; i++){
            for (int j = i+1; j<num.length; j++){
                if (sum - num[i] - num[j] == 100){
                    for (int k = 0; k<num.length; k++){
                        if (i == k || j == k){
                            continue;
                        }
                        System.out.println(num[k]);
                    }
                    System.exit(0);
                }
            }
        }
        sc.close();
    }
}


