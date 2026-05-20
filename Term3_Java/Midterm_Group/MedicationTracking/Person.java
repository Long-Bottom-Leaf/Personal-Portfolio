package MedicationTracking;

import java.util.concurrent.atomic.AtomicInteger;

/**
 * Abstract base class representing a generic person.
 * Serves as a superclass for both Doctor and Patient.
 */
public abstract class Person {
    private static final AtomicInteger ID_GEN = new AtomicInteger(0);
    private final int id;
    protected String name;
    protected int age;
    protected String phoneNumber;

    /**
     * Constructs a new Person with the given attributes.
     *
     * @param name         the person's name
     * @param age          the person's age
     * @param phoneNumber  the contact phone number
     */
    public Person(String name, int age, String phoneNumber) {
        this.id = ID_GEN.getAndIncrement();
        this.name = name;
        this.age = age;
        this.phoneNumber = phoneNumber;
    }

    /** @return the person's unique ID */
    public int getId() {
        return id;
    }

    /** @return the person's name */
    public String getName() {
        return name;
    }

    /** @return the person's age */
    public int getAge() {
        return age;
    }

    /** @return the person's phone number */
    public String getPhoneNumber() {
        return phoneNumber;
    }

    /** @param name sets the person's name */
    public void setName(String name) {
        this.name = name;
    }

    /** @param age sets the person's age (must be positive) */
    public void setAge(int age) {
        if (age > 0) this.age = age;
    }

    /** @param phoneNumber sets the person's contact number */
    public void setPhoneNumber(String phoneNumber) {
        this.phoneNumber = phoneNumber;
    }

    @Override
    public String toString() {return String.format("ID:%d Name:%s Age:%d Phone:%s", id, name, age, phoneNumber);
    }
}
