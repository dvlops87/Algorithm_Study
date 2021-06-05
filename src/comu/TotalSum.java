package comu;

import java.util.Scanner;

public class TotalSum {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("숫자를 입력하세요: ");
        int num = sc.nextInt();
        int total = 0;

        /* for문으로 구현 */
        for (int i = 1; i<=num; i++){
            total += i;
        }
        System.out.printf("1부터 %d까지의 합은 %d입니다! \n",num, total);

        /* while문으로 구현 */
        int j = 0;
        total = 0;
        while(j <= num){
            total += j;
            j++;
        }
        System.out.printf("1부터 %d까지의 합은 %d입니다! ",num, total);

        /* 구구단 출력 */

        for (int i=1; i<num; i++){
            for (j=1; j<10; j++){
                System.out.printf("%d * %d = %d\n", i ,j, i*j);
            }
        }



        sc.close();
    }
}
