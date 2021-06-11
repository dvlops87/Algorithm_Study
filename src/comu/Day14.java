package comu;

import java.util.InputMismatchException;
import java.util.Scanner;

public class Day14 {


    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int [] value = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10};

        while (true){
            System.out.print("숫자를 입력하세요: ");
            try {
                int i = sc.nextInt();
                System.out.println(value[i]);
                System.out.println("프로그램 종료");
                break;
            }
            /* 입력값이 정수가 아닐 경우 */
            catch (InputMismatchException e){
                System.out.println("( 입력 오류 )숫자를 입력하세요!");
                System.exit(0);
            }
            /* 배열의 범위를 벗어난 경우 */
            catch (ArrayIndexOutOfBoundsException e){
                System.out.println("0~9 사이의 값을 입력하세요");
            }
        }
        sc.close();
    }
}
