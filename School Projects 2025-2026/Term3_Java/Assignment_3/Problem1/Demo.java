package Problem1;

/**
 * The Demo class tests the Person, Student, Teacher, and CollegeStudent
 * classes by creating objects and displaying their string representations.
 * 
 * This serves as the entry point for the application.
 * 
 * @author Stephen
 */
public class Demo {
    public static void main(String[] args) {
        // Create a Person
        Person bob = new Person("Coach Bob", 27, "M");
        System.out.println("\n" + bob);

        // Create a Student
        Student lynne = new Student("Lynne Brooke", 16, "F", "HS95129", 3.5);
        System.out.println("\n" + lynne);

        // Create a Teacher
        Teacher mrJava = new Teacher("Duke Java", 34, "M", "Computer Science", 50000);
        System.out.println("\n" + mrJava);

        // Create a CollegeStudent
        CollegeStudent ima = new CollegeStudent("Ima Frosh", 18, "F", "UCB123", 4.0, 1, "English");
        System.out.println("\n" + ima);
    }
}
