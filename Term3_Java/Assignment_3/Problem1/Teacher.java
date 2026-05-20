package Problem1;

/**
 * The Teacher class extends the Person class and represents a teacher.
 * It includes additional attributes for the subject taught and annual salary.
 * 
 * This class demonstrates the use of inheritance and the super keyword.
 * 
 * @author Stephen
 */
public class Teacher extends Person {
    private String mySubject; // subject taught by the teacher
    private double mySalary;  // annual salary of the teacher

    /**
     * Constructs a Teacher object with the specified attributes.
     * 
     * @param name    the teacher's name
     * @param age     the teacher's age
     * @param gender  the teacher's gender
     * @param subject the subject taught
     * @param salary  the teacher's salary
     */
    public Teacher(String name, int age, String gender, String subject, double salary) {
        super(name, age, gender);
        mySubject = subject;
        mySalary = salary;
    }

    /** @return the subject taught */
    public String getSubject() {
        return mySubject;
    }

    /** @return the teacher's salary */
    public double getSalary() {
        return mySalary;
    }

    /** @param subject sets the subject taught */
    public void setSubject(String subject) {
        mySubject = subject;
    }

    /** @param salary sets the teacher's salary */
    public void setSalary(double salary) {
        mySalary = salary;
    }

    /**
     * Returns a string representation of the Teacher object.
     * 
     * @return a formatted string containing the teacher's details
     */
    public String toString() {
        String formattedSalary = String.format("$%,.2f", mySalary);
        return super.toString() + ", subject: " + mySubject + ", salary: " + formattedSalary;
    }
}
