package Problem1;

/**
 * The Person class represents a generic person with basic attributes such as
 * name, age, and gender. This class serves as a superclass for more specific
 * types of people like Student and Teacher.
 * 
 * @author Stephen
 */
public class Person {
    // Instance variables
    protected String myName;   // name of the person
    protected int myAge;       // age of the person
    protected String myGender; // "M" for male, "F" for female

    /**
     * Constructs a Person object with the specified name, age, and gender.
     * 
     * @param name   the person's name
     * @param age    the person's age
     * @param gender the person's gender
     */
    public Person(String name, int age, String gender) {
        myName = name;
        myAge = age;
        myGender = gender;
    }

    /** @return the person's name */
    public String getName() {
        return myName;
    }

    /** @return the person's age */
    public int getAge() {
        return myAge;
    }

    /** @return the person's gender */
    public String getGender() {
        return myGender;
    }

    /** @param name sets the person's name */
    public void setName(String name) {
        myName = name;
    }

    /** @param age sets the person's age */
    public void setAge(int age) {
        myAge = age;
    }

    /** @param gender sets the person's gender */
    public void setGender(String gender) {
        myGender = gender;
    }

    /**
     * Returns a string representation of the Person object.
     * 
     * @return a formatted string containing the person's details
     */
    public String toString() {
        return myName + ", age: " + myAge + ", gender: " + myGender;
    }
}
