package comu;

class Calculator {
    public int x,y;

    public int add(){
    return x+y;
    }
    public int sub(){
        return x-y;
    }
    public int div(){
        return x/y;
    }
    public int mul(){
        return x*y;
    }
    public void printResult(int num){
        switch (num){
            case 1:
                System.out.printf("%d + %d = %d\n",x,y,add());
                break;
            case 2:
                System.out.printf("%d - %d = %d\n",x,y,sub());
                break;
            case 3:
                System.out.printf("%d // %d = %d\n",x,y,div());
                break;
            case 4:
                System.out.printf("%d * %d = %d\n",x,y,mul());
                break;
            default:
                System.out.println("번호를 잘못입력하셨어요");
        }
    }
}

public class Day12 {
    public static void main(String[] args) {
        Calculator calculator = new Calculator();
        calculator.x = 30;
        calculator.y = 50;
        calculator.printResult(1);
        calculator.printResult(2);
        calculator.printResult(3);
        calculator.printResult(4);
        calculator.printResult(5);
    }
}
