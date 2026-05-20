package Term3.Java.QAP2.Problem1;        // may need to edit or delete this line to run

public class CreditCard {
    private Money balance;
    private Money creditLimit;
    private Person owner;

    // default constructor for credit card owner and limit
    public CreditCard(Person owner, Money creditLimit) {
        this.owner = owner;
        this.creditLimit = creditLimit;
        this.balance = new Money(0);
    }

    // accessors
    public Money getBalance() {
        return new Money(balance);          // returns a copy of balance, this way we can avoid accidentally changing the balance outside of this class
    }

    public Money getCreditLimit() {
        return new Money(creditLimit);      // returns a copy of creditLimit, this way we can avoid accidentally changing the creditLimit outside of this class
    }

    public String getPersonals() {
        return owner.toString();
    }

    // charge method
    public void charge(Money amount) {
        Money newBalance = balance.add(amount);

        // in Money class, -1 or 0 means less than or equal to the credit limit, so here we check if the balance plus the charge is less than or equal to the credit limit
        if (newBalance.compareTo(creditLimit) <= 0) {
            balance = newBalance;
            System.out.println("Charge approved! Charged: " + amount);
            // System.out.println("New balance: " + balance);           // commented out to conform with expected testing code, would print twice, left in if we want to change later

        } else {
            System.out.println("Charge denied. Exceeds credit limit.");
        }
    }

    // payment on credit card method
    public void payment(Money amount) {
        balance = balance.subtract(amount);

        System.out.println("Payment accepted! Payed: " + amount);
        // System.out.println("New balance: " + balance);              // commented out to conform with expected testing code, would print twice, left in if we want to change later
    }
}