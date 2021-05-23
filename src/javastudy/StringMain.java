package javastudy;
public class StringMain {
    public static void main(String[] args) {
        String city1="Asia";    // String은 참조타입이지만 new 키워드 사용 안하고 생성 가능
        String city2="Europe";
        String city3= new String("Asia");
        String city7="Asia";
        System.out.println(city1);
        System.out.println(city1.length());
        System.out.println(city1==city2);   // Asia == Europe ==> false
        System.out.println(city1.equals(city2));
        System.out.println(city1==city3);   // new 키워드 아닌 Asia == new 키워드 Asia F
        System.out.println(city1==city7);   // new 키워드 아닌 Asia == new 키워드 아닌 Asia T
        System.out.println(city1.equals(city3)); // new 키워드 아닌 Asia.equals(new키워드 Asia) T
        System.out.println(city1.equals(city7)); // new 키워드 아닌 Asia.equals(new키워드 아닌  Asia) T
        /* 0523 스터디*/
        /*  .equals() 는 해시 코드를 비교하고  == 는 레퍼런스를 비교한다. */

        String city4 = String.format("%s-%s", city1,city2);
        System.out.println(city4);
        String city5 = city1 + "-" + city2 + 1 + 2;
        System.out.println(city5);
        String city6 = 1 + 2 + city1 + "-" + city2;
        System.out.println(city6);
    }
}
