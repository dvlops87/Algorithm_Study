package comu;

public class PrintEx {
    public static void main(String[] args) {

        int a = 10;
        int b = 30;
        System.out.println("-----------------------------");  
        System.out.println("덧셈, 뺄셈, 곱셈의 결과를 볼까요?");  
        System.out.print(" a+b는 ");                        
        System.out.printf("%d,",a+b);                      // 지시자 사용
        System.out.print(" a-b는 ");
        System.out.printf("%d,",a-b);
        System.out.print(" a*b는 ");
        System.out.printf("%d\n",a*b);                     //개행문자 사용
        System.out.println("-----------------------------");


    }
}
