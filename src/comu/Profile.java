package comu;

import java.util.Scanner;

public class Profile {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("======== 자기소개 입력하기 =========");

        System.out.print("이름을 입력하세요: ");
        String name = sc.nextLine();

        System.out.print("나이를 입력하세요: ");
        int age = sc.nextInt();
        sc.nextLine();

        System.out.print("혈액형을 입력하세요: ");
        String bloodtype = sc.nextLine();

        System.out.print("키를 입력하세요: ");
        float height = sc.nextFloat();
        sc.nextLine();

        System.out.print("MBTI를 입력하세요: ");
        String MBTI = sc.nextLine();

        System.out.print("좌우명 한 문장을 입력하세요: ");
        String motto = sc.nextLine();

        System.out.println("======== 자기소개 입력 완료 =========\n\n");
        System.out.println("아이엠 그라운드 자기소개 시작! => 시작하려면 엔터를 누르세요.");
        sc.nextLine();

        System.out.printf("저는 %s입니다. 나이는 %d살 이예요.\n",name ,age);
        System.out.printf("혈액형은 %s형 이구요, 키는 %.1f(cm)이고 MBTI는 %s입니다.\n\n",bloodtype, height, MBTI);

        System.out.printf("★★★%s!!!!!!!!!★★★", motto);

    }
}
