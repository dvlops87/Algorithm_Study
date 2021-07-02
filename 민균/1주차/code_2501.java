package baekjoon.study.week1;

import java.util.ArrayList;
import java.util.Scanner;

public class n2501 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        ArrayList<Integer> Arr = new ArrayList<Integer>();
        int N,K;
        N = sc.nextInt();
        K = sc.nextInt();

        for (int i = 1; i<=N; i++){
            if(N % i== 0){
                Arr.add(i);
            }
        }

        System.out.println(Arr.get(K-1));
    }
}