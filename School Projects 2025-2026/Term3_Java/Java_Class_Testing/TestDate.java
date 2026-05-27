package Term_3.Assignment_1;

public class TestDate {
    public static void main(String[] args) {

        // Test 1: Valid date creation

        Date d1 = new Date(21, 9, 2025); 
        System.out.println("\nDate: " + d1.toString());

        // Test 2: Change the date to a valid new one

        d1.setDate(1, 1, 2026);
        System.out.println("Updated Date: " + d1.toString());

        // Test 3: Invalid month (should print error and keep old value)

        d1.setDate(10, 13, 2025); 
        System.out.println("After invalid month input (13): " + d1.toString());

        // Test 4: Invalid day for given month (April 31st)

        d1.setDate(31, 4, 2025); 
        System.out.println("After invalid day input (31 April): " + d1.toString());

        // Test 5: February 29 on a leap year (valid)

        d1.setDate(29, 2, 2024); 
        System.out.println("Leap year date (29/02/2024): " + d1.toString());

        // Test 6: February 29 on a non-leap year (invalid)

        d1.setDate(29, 2, 2023); 
        System.out.println("Non-leap year date (29/02/2023): " + d1.toString());
    }
}
