package comu;

class Student {
    String name;
    int math, eng, kor;

    Student(String name, int math, int eng, int kor) {
        this.name = name;
        this.math = math;
        this.eng = eng;
        this.kor = kor;
    }
/* 평균 점수를 구하는 메서드 */
    public float getAverage() {
        return (float)(math+eng+kor)/3;
    }
/* 평균 점수를 출력하는 메서드 */
    public void printAverage() {
        System.out.printf("%s의 평균 점수 : %.3f\n", name, getAverage());
    }
}
public class Day13 {
    public static void main(String[] args) {
        Student student1 = new Student("균민이", 100, 87, 99);
        Student student2 = new Student("코뮤", 79, 88, 99);

        student1.printAverage();
        student2.printAverage();
    }
}
