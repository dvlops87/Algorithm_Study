package baekjoon.study.week1;

import java.util.Scanner;

public class n3460 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int T,n;
        T = sc.nextInt();

        for (int i = 0; i<T; i++){
            n = sc.nextInt();
            String num = Integer.toBinaryString(n); //입력받은 10진수를 2진수로 변환 후 문자열에 저장
            StringBuffer sb = new StringBuffer(num); //reversed() 메서드를 사용하기 위해 StringBuffer 객체에 옮긴 후
            String reversed_num = sb.reverse().toString(); //reversed()사용 후 새로운 문자열 reversed_num 에 저장

            for (int j = 0; j<reversed_num.length(); j++){ // 문자열 하나 씩 1이 맞는지 비교
                if(reversed_num.charAt(j) == '1'){
                    System.out.print(j+" ");
                }
            }
        }

        sc.close();
    }
}
