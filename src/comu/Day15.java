package comu;

class NumberThread extends Thread{
    public void run(){
        // 0부터 49까지 출력
        for (int i = 0; i < 50; i++){
            System.out.print(i);
        }
    }
}
class CharThread extends Thread{
    public void run(){
        //a부터 z까지 출력
        for (char i = 'a'; i <= 'z'; i++){
            System.out.print(i);
        }
    }
}

public class Day15 {
    public static void main(String[] args) {
        //NumberThread 클래스 인스턴스 생성
        Thread thread1 = new NumberThread();
        //CharThread 클래스 인스턴스 생성
        Thread thread2 = new CharThread();

        thread1.start(); // NumberThread 시작
        thread2.start(); // CharThread 시작
    }
}
