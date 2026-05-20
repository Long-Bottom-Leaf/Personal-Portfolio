package Term3.Java.QAP2.Problem1;        // may need to edit or delete this line to run

public class CreditCardDemo {
    public static void main(String[] args) {

        // test constants
        final Money LIMIT = new Money(1000);
        final Money FIRST_AMOUNT = new Money(200);
        final Money SECOND_AMOUNT = new Money(10.02);
        final Money THIRD_AMOUNT = new Money(25);
        final Money FOURTH_AMOUNT = new Money(990);

        // test owner, extra System.out.println("\n"); in tests is simply for readability
            System.out.println("\n");
            
            Person owner = new Person("Christie", "Diane", new Address("237J Harvey Hall", "Menomonie", "WI", "54751"));

        // assigning the credit card to the owner details
            CreditCard visa = new CreditCard(owner, LIMIT);

        // test initial values
            System.out.println("\n");
            
            System.out.println(visa.getPersonals());
            System.out.println("Balance: " + visa.getBalance());
            System.out.println("Credit Limit: " + visa.getCreditLimit());
            System.out.println();

        // test attempting charges for first amount
            System.out.println("\n");

            System.out.println("Attempt to charge " + FIRST_AMOUNT);
            visa.charge(FIRST_AMOUNT);
            System.out.println("Balance: " + visa.getBalance());

        // test attempting charges for second amount
            System.out.println("\n");
            
            System.out.println("Attempt to charge " + SECOND_AMOUNT);
            visa.charge(SECOND_AMOUNT);
            System.out.println("Balance: " + visa.getBalance());

        // test attempting payment for third amount
            System.out.println("\n");

            System.out.println("Attempt to pay " + THIRD_AMOUNT);
            visa.payment(THIRD_AMOUNT);
            System.out.println("Balance: " + visa.getBalance());

        // test attempting charges for fourth amount
            System.out.println("\n");
            
            System.out.println("Attempt to charge " + FOURTH_AMOUNT);
            visa.charge(FOURTH_AMOUNT);
            System.out.println("Balance: " + visa.getBalance());
    }
}