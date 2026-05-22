package Problem1;

/**
 * The Student class represents a student and extends the Person class.
 * It adds attributes for a student ID number and grade point average (GPA).
 * 
 * This class demonstrates inheritance by adding new fields and methods while
 * reusing functionality from the Person superclass.
 * 
 * @author Stephen
 */
public class Student extends Person {
    protected String myIdNum;  // student ID number
    protected double myGPA;    // grade point average

    /**
     * Constructs a Student object with the specified attributes.
     * 
     * @param name   the student's name
     * @param age    the student's age
     * @param gender the student's gender
     * @param idNum  the student's ID number
     * @param gpa    the student's GPA
     */
    public Student(String name, int age, String gender, String idNum, double gpa) {
        super(name, age, gender);  // call Person constructor
        myIdNum = idNum;
        myGPA = gpa;
    }

    /** @return the student's ID number */
    public String getIdNum() {
        return myIdNum;
    }

    /** @return the student's GPA */
    public double getGPA() {
        return myGPA;
    }

    /** @param idNum sets the student's ID number */
    public void setIdNum(String idNum) {
        myIdNum = idNum;
    }

    /** @param gpa sets the student's GPA */
    public void setGPA(double gpa) {
        myGPA = gpa;
    }

    /**
     * Returns a string representation of the Student object.
     * 
     * @return a formatted string containing the student's details
     */
    public String toString() {
        return super.toString() + ", ID: " + myIdNum + ", GPA: " + myGPA;
    }
}
