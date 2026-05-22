package Term3.Java.QAP1; // This file location will need to be changed or deleted before running

public class Date {
    
    // Instance variables

    private int day;
    private int month;
    private int year;
    
    // Date constructor

    public Date(int day, int month, int year) {
        setDate(day, month, year);
    }

    // Accessors

    public int getDay() {
        return day;
    }

    public int getMonth() {
        return month;
    }

    public int getYear() {
        return year;
    }

    // Setters

    public void setDay(int day) {
        this.day = day;
    }

    public void setMonth(int month) {
        this.month = month;
    }

    public void setYear(int year) {
        this.year = year;
    }

    public void setDate(int day, int month, int year) {

        if (month < 1 || month > 12) {
            System.out.println(month + " is an invalid month.");
            return;
        }

        // Days per month (February = 28)

        int[] daysInMonth = {31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31};

        // Leap year adjustment for February

        if ((year % 4 == 0 && year % 100 != 0) || (year % 400 == 0)) {
            daysInMonth[1] = 29; // February index = 1
        }

        // Check months
        
        if (day < 1 || day > daysInMonth[month - 1]) {
            System.out.println("Invalid day " + day + " for month " + month);
            return;
        }

        // If everything is valid

        this.day = day;
        this.month = month;
        this.year = year; 
    }

    @Override           // Tells Java how to output the information in a readable format
    public String toString() {
        return String.format("%02d/%02d/%04d", day, month, year);
    }
}