package Term_3.Assignment_1;

public class TestTime {
    
    public static void main(String[] args) {

        // Initial time objects

        Time t1 = new Time(21, 10, 15);
        Time t2 = new Time(10, 20, 25);

        System.out.println("\nInitial Times: ");
        System.out.println("Hours: " + t1.getHour() + " Minutes: " + t1.getMinute() + " Seconds: " + t1.getSecond());
        System.out.println("Hours: " + t2.getHour() + " Minutes: " + t2.getMinute() + " Seconds: " + t2.getSecond());

        // Advance and rewind

        t1.nextSecond();
        t2.previousSecond();

        System.out.println("\nAfter modifications:");
        System.out.println("Time 1 (after +1 sec): " + t1);
        System.out.println("Time 2 (after -1 sec): " + t2);

        // Test 1 Roll over next hour / day

        Time t3 = new Time(23, 59, 59);
        System.out.println("\nBefore nextSecond() (midnight roll over): " + t3);
        t3.nextSecond();

        System.out.println("After nextSecond(): " + t3);  // Expect 00:00:00

        // Test 2 rewind to previous minute

        Time t4 = new Time(14, 0, 0);
        System.out.println("\nBefore previousSecond() (minute rewind): " + t4);
        t4.previousSecond();

        System.out.println("After previousSecond(): " + t4);  // Expect 13:59:59

        //  Test 3 Rewind to previous hour

        Time t5 = new Time(0, 0, 0);
        System.out.println("\nBefore previousSecond() (rewind to previous day): " + t5);
        t5.previousSecond();

        System.out.println("After previousSecond(): " + t5);  // Expect 23:59:59

        // Test 4 setTime() method

        Time t6 = new Time(0, 0, 0);
        System.out.println("\nBefore setTime(): " + t6);

        t6.setTime(8, 30, 45);
        System.out.println("After setTime(8, 30, 45): " + t6);
    }
}