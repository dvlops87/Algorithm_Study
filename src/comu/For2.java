package comu;

import java.util.Scanner;

public class For2 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int[] num = new int[5];
        System.out.print("숫자 5개를 띄어쓰기로 구분하여 입력하세요: ");
        for (int i = 0; i<5; i++){
            num[i] = sc.nextInt();
        }
        System.out.println("====입력 완료====");
        System.out.println("====출력 시작====");
        for (int j = 4; j>=0; j--) {
            System.out.printf("%d\n", num[j]);
        }
    }
}
