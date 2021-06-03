package comu;

import java.util.Scanner;

public class Operator3 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in); //.useDelimiter("\\s|,");

        System.out.print("숫자 2개를 입력하세요: ");  //Scanner 의 디폴트 구분자는 space다!
        int num1 = sc.nextInt();
        int num2 = sc.nextInt();
        int Big_num = 0;

        sc.close();
        /* 두 수를 비교하여 더 큰 값을 Big num 에다가 저장 */
        if (num1 > num2) {
            Big_num = num1;
        } else if (num1 < num2) {
            Big_num = num2;
        }

        //Big_num이 0으로 초기화한 상태 그대로라면 두 수가 같음을 의미
        System.out.print("둘 중에 큰 수는 : ");
        System.out.println(Big_num != 0 ? Big_num : "같음");
    }
}
