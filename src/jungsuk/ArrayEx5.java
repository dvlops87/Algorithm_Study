package jungsuk;

import java.util.Scanner;

public class ArrayEx5 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int sum = 0; //총점 저장
        float average = 0f; //평균 저장

        int [] score = new int[5];

        for (int i = 0; i < score.length; i++){
            System.out.print("점수를 입력하세요: ("+(i+1)+")번 입력");
            score[i] = sc.nextInt();
            sum += score[i];
        }

    average = sum/(float)score.length;

        System.out.println("총점 : " + sum);
        System.out.println("평균 : " + average);

    }
}
