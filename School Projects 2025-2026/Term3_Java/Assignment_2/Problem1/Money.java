package Term3.Java.QAP2.Problem1;        // may need to edit or delete this line to run

public class Money implements Comparable<Money> {       // we are telling the class object to be able to compare to another object of the same class
    private long dollars;                               // long allows larger numbers for money calculations
    private long cents;

    // default constructor for money object
    public Money(double amount) {
        long totalCents = Math.round(amount * 100);     // round totalCents to remove rounding errors
        this.dollars = totalCents / 100;
        this.cents = totalCents % 100;
    }

    // copy constructor
    public Money(Money other) {
        this.dollars = other.dollars;
        this.cents = other.cents;
    }

    // adding money method
    public Money add(Money otherAmount) {
        long totalCents = (this.dollars * 100 + this.cents) + (otherAmount.dollars * 100 + otherAmount.cents);      // we want to convert everything to cents as it makes it easier to do the calculations without rounding errors, convert back later
        return new Money(totalCents / 100.0);
    }

    // subtracting money method
    public Money subtract(Money otherAmount) {
        long totalCents = (this.dollars * 100 + this.cents) - (otherAmount.dollars * 100 + otherAmount.cents);      // we want to convert everything to cents as it makes it easier to do the calculations without rounding errors, convert back later
        return new Money(totalCents / 100.0);
    }

    // compareing method
    public int compareTo(Money otherAmount) {
        double thisTotal = this.dollars + this.cents / 100.0;
        double otherTotal = otherAmount.dollars + otherAmount.cents / 100.0;

        // we cannot return true/fales for a 3 option comparison, so we will use -1, 0, 1
        if (thisTotal < otherTotal) {
            return -1;

        } else if (thisTotal > otherTotal) {
            return 1;

        } else {
            return 0;

        }
    }

    // equals method
    public boolean equals(Money otherObject) {
        return (this.dollars == otherObject.dollars && this.cents == otherObject.cents);
    }

    // toString method
    public String toString() {
        return String.format("$%,.2f", (dollars + cents / 100.0));
    }
}