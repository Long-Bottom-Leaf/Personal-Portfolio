package Term3.Java.QAP2.Problem1;        // may need to edit or delete this line to run

public class Person {
    private String firstName;
    private String lastName;
    private Address home;
    
    public Person(String firstName, String lastName, Address home) {
        this.firstName = firstName;
        this.lastName = lastName;
        this.home = home;
    }

    public String toString() {
        return firstName + " " + lastName + "\n" + home.toString();
    }
}
