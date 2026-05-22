package Term3.Java.QAP1;        // This file location will need to be changed or deleted, please edit before running

public class TestAccount {

    public static void main(String [] args) {

        // Test accounts
        Account acc1 = new Account("638", "Johnny Jones", 5000);
        Account acc2 = new Account("397", "April Brooks", 4000);

        // Display balances

        System.out.println("\nInitial Balances:");
        printAccount(acc1);
        printAccount(acc2);

        // Test 1: Valid transfer

        acc1.transferTo(acc2, 1000);
        System.out.println("\nAfter transferring $1000 from Johnny to April:");
        printAccount(acc1);
        printAccount(acc2);

        // Test 2: Deposit into an account

        acc1.credit(500);       // Johnny deposits $500
        System.out.println("\nAfter Johnny deposits $500:");
        printAccount(acc1);

        // Test 3: Withdraw from an account

        acc2.debit(1500);       // April withdraws $1500
        System.out.println("\nAfter April withdraws $1500:");
        printAccount(acc2);

        // Test 4: Overdraft attempt (withdraw more than balance)

        acc2.debit(10000);      // Invalid
        System.out.println("\nAttempting to withdraw $10,000 from April:");
        printAccount(acc2);

        // Test 5: Transfer more than available

        acc1.transferTo(acc2, 10000);       // Invalid
        System.out.println("\nAttempting to transfer $10,000 from Johnny to April:");
        printAccount(acc1);
        printAccount(acc2);

        // Test 6: Negative deposit (should reject)

        acc1.credit(-200);
        System.out.println("\nAttempting to deposit -$200 into Johnny’s account:");
        printAccount(acc1);

        // Test 7: Negative withdraw (should reject)

        acc2.debit(-500);
        System.out.println("\nAttempting to withdraw -$500 from April’s account:");
        printAccount(acc2);

        // Test 8: Final account states

        System.out.println("\nFinal account states:");
        printAccount(acc1);
        printAccount(acc2);
    }

    // A method to keep app print formatting consistent

    private static void printAccount(Account acc) {
        System.out.println("Account ID: " + acc.getID() + " Name: " + acc.getName() + " Balance: $" + acc.getBalance());
    }
}
