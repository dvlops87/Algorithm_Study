package part2;

/*API에서 제공하는 참조타입 사용하기 */
import java.util.Calendar;
import java.util.Date;
public class JavaObjectType {
    public static void main(String[] args) {
        //기본타입의 배열은 참조형
        int [] m = {1,2,3}; //배열
        int [] n = new int[] {1,2,3}; //배열

        //참조타입 - 객체타입
        String card = "H8"; //문자열
        Date d = new Date(); //오늘
        Calendar cal = Calendar.getInstance(); //오늘
        //자동으로 toString() 이 붙음
        System.out.println(card); // card.toString()
        System.out.println(d);  // d.toString()
        System.out.println(cal); // cal.toString()

    }
}
