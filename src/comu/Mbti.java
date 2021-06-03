package comu;

import java.util.Scanner;

public class Mbti {
    public static void main(String[] args) {
        System.out.println("==== 개발자 MBTI 결과 보기 ====");
        Scanner sc = new Scanner(System.in);
        System.out.print("당신의 MBTI를 입력하세요: ");
        String MBTI = sc.nextLine();

        switch (MBTI){
            case "INTP":
            case "intp":
                System.out.println("당신은 백엔드형입니다!");
                break;
            case "ENFJ":
            case "enfj":
                System.out.println("당신은 프론트엔드형입니다!");
                break;
            case "INFJ":
            case "infj":
                System.out.println("당신은 풀스택형입니다!");
                break;
            case "ISTJ":
            case "istj":
                System.out.println("당신은 퍼블리셔형입니다!");
                break;
            case "ENTJ":
            case "entj":
                System.out.println("당신은 아키텍쳐형입니다!");
                break;
            case "ISFJ":
            case "isfj":
                System.out.println("당신은 보안전문가형입니다!");
                break;
            case "INTJ":
            case "intj":
                System.out.println("당신은 데이터분석가형입니다!");
                break;
            case "ENFP":
            case "enfp":
                System.out.println("당신은 AI형입니다!");
                break;
            case "ENTP":
            case "entp":
                System.out.println("당신은 iOS형입니다!");
                break;
            case "ESFJ":
            case "esfj":
                System.out.println("당신은 안드로이드형입니다!");
                break;
            case "ESFP":
            case "esfp":
                System.out.println("당신은 게임개발자형입니다!");
                break;
            case "ESTP":
            case "estp":
                System.out.println("당신은 ioT개발형입니다!");
                break;
            case "ESTJ":
            case "estj":
                System.out.println("당신은 QA형입니다!");
                break;
            case "INFP":
            case "infp":
                System.out.println("당신은 블록체인형입니다!");
                break;
            case "ISTP ":
            case "istp":
                System.out.println("당신은 임베디드 개발자형입니다!");
                break;
            case "ISFP":
            case "isfp":
                System.out.println("당신은 네트워크 개발자형입니다!");
                break;
            default:
                System.out.println("정확한 MBTI유형이 아니네요 ㅠ.ㅠ");


        }
        sc.close();
    }

}
