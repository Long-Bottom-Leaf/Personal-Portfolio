package Problem1;

/**
 * The CollegeStudent class extends the Student class and represents
 * a college-level student. It includes additional attributes for
 * the student's current academic year and declared major.
 * 
 * This class further extends the concept of inheritance from Student.
 * 
 * @author Stephen
 */
public class CollegeStudent extends Student {
    private int myYear;     // year in college (1=FROSH, 2=SOPH, etc.)
    private String myMajor; // student's major field of study

    /**
     * Constructs a CollegeStudent object with the specified attributes.
     * 
     * @param name   the student's name
     * @param age    the student's age
     * @param gender the student's gender
     * @param idNum  the student's ID number
     * @param gpa    the student's GPA
     * @param year   the student's current year in college
     * @param major  the student's declared major
     */
    public CollegeStudent(String name, int age, String gender, String idNum, double gpa, int year, String major) {
        super(name, age, gender, idNum, gpa);
        myYear = year;
        myMajor = major;
    }

    /** @return the student's current year in college */
    public int getYear() {
        return myYear;
    }

    /** @return the student's major */
    public String getMajor() {
        return myMajor;
    }

    /** @param year sets the student's year */
    public void setYear(int year) {
        myYear = year;
    }

    /** @param major sets the student's major */
    public void setMajor(String major) {
        myMajor = major;
    }

    /**
     * Returns a string representation of the CollegeStudent object.
     * 
     * @return a formatted string containing the college student's details
     */
    public String toString() {
        return super.toString() + ", year: " + myYear + ", major: " + myMajor;
    }
}
