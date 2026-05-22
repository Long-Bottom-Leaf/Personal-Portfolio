package Term3.Java.QAP1;        // This file location will need to be changed or deleted, please edit before running

public class Account {

    // Instance variables

    private String id;
    private String name;
    private int balance = 0;    // set starting balance as 0

    // Constructor with Id and Name

    public Account(String id, String name) {
        
        this.id = id;
        this.name = name;
    }

    // Constructor with Id, Name, and balance

    public Account(String id, String name, int balance) {

        this.id = id;
        this.name = name;
        this.balance = balance;
    }

    // Accessors

    public String getID() {
        return id;
    }

    public String getName() {
        return name;
    }

    public int getBalance() {
        return balance;
    }

    // Methods

    public int credit(int amount) {         // adds the credited amount to the account balance
        balance += amount;
        return balance;
    }

    public int debit(int amount) {
        if (amount <= balance) {
            balance -= amount;
        } else {
            System.out.println("Amount exceeded balance!");
        }

        return balance;
    }

    public int transferTo(Account another, int amount) {
        if (amount <= balance) {
            this.balance -= amount;         // specifiying this account -
            another.balance += amount;      // specifiying another account +
        } else {
            System.out.println("Amount exceeded balance!");
        }

        return balance;
    }

    @Override                       // this is just telling java how to output in a human readable format
        public String toString() {
            return "Account[id=" + id + ", name=" + name + ", balance=" + balance + "]";
        }
}