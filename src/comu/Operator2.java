package comu;

public class Operator2 {
    public static void main(String[] args) {
        int a = 3;
        int b = 5;
        System.out.printf("%d %d %d", ++a + b--, a, ++b);
        // ++a + b-- = 9,  a(3)에 1을 더하고 나서 b(5)와 더한 후 출력하고, b(5)에서 -1을 해준다 , b(4)
        // a = 4        ,  a(4)를 출력한다.
        // ++b = 5      ,  b(4)에 1을 더하고 나서 b(5)를 출력한다.
    }
}
