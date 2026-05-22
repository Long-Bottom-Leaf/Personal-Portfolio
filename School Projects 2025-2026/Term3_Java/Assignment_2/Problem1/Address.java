package Term3.Java.QAP2.Problem1;        // may need to edit or delete this line to run

public class Address {
    private String street;
    private String city;
    private String state;
    private String zip;

    // address method
    public Address(String street, String city, String state, String zip) {
        this.street = street;
        this.city = city;
        this.state = state;
        this.zip = zip;
    }

    // to string method
    public String toString() {
        return street + ", " + city + ", " + state + " " + zip;
    }
}
